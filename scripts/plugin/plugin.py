import enum
import functools
from json import JSONDecodeError
from pathlib import Path
from typing import Optional, List, Dict, Union, Callable, Any, Type, TypeVar

from typing_extensions import Literal

from common import constants, log
from common.report import reporter
from common.translation import Text, BundledText, LANGUAGES, get_file_name, with_language
from meta.author import Author
from meta.plugin import PluginInfo, MetaInfo
from meta.plugin_all import AllOfAPlugin
from meta.release import ReleaseSummary
from meta.repos import RepositoryInfo
from meta.request_meta import RequestMeta, REQUEST_META_DEFAULT_TTL
from plugin.cache import PluginRequestCacheManager
from plugin.label import Label, get_label_set
from utils import file_utils, markdown_utils
from utils.repos import PLUGIN_CATALOGUE, GithubRepository
from utils.serializer import Serializable

_S = TypeVar('_S', bound=Serializable)


class _PluginDataSet(enum.Flag):
	info = enum.auto()
	introduction = enum.auto()
	meta = enum.auto()
	releases = enum.auto()
	repository = enum.auto()

	def is_everything_fetched(self) -> bool:
		for ds in _PluginDataSet:
			if ds not in self:
				return False
		return True


class _PluginInfoJson(Serializable):
	"""
	Content of plugin_info.json
	"""
	id: str
	authors: List[Union[str, Author]] = []
	repository: str
	branch: str
	related_path: str = '.'
	labels: List[str] = []
	introduction: Dict[str, str] = {}  # lang -> file path in repos


class _PluginInfoInternal:
	id: str

	repos: GithubRepository
	branch: str
	related_path: Optional[str]

	labels: List[Label]
	authors: List[Author]
	external_introduction: Dict[str, str]

	disable: bool
	disable_reason: str

	def __init__(self, plugin_json: dict):
		info = _PluginInfoJson.deserialize(plugin_json)

		self.id = info.id
		self.repos = GithubRepository(info.repository, info.branch, info.related_path)

		self.authors = []
		for item in info.authors:
			assert isinstance(item, (str, Author)), 'author item should be str or Author, found {}'.format(type(item))
			if isinstance(item, str):
				author = Author()
				author.name = item
			else:
				author = item
			self.authors.append(author)

		# label
		self.labels = []
		for label_key in info.labels:
			label = get_label_set().get_label(label_key)
			if label is None:
				raise ValueError('Unknown label: {}'.format(label_key))
			else:
				self.labels.append(label)

		# introduction
		self.external_introduction = info.introduction

		# disable state
		self.disable = bool(plugin_json.get('disable'))
		self.disable_reason = str(plugin_json.get('disable_reason', 'unknown'))


class Plugin:
	__plugin_info: _PluginInfoInternal

	# might be null, if repos not found
	meta_info: Optional[MetaInfo] = None
	release_summary: Optional[ReleaseSummary] = None
	repository_info: Optional[RepositoryInfo] = None

	def __init__(self, plugin_id: str):
		self.__introduction: Optional[BundledText] = None

		self.__info_directory = Path(constants.PLUGINS_FOLDER) / plugin_id
		if not self.__info_directory.is_dir():
			raise FileNotFoundError('Directory {} not found'.format(self.__info_directory))

		plugin_json = file_utils.load_json(self.__info_directory / 'plugin_info.json')
		self.__plugin_info = _PluginInfoInternal(plugin_json)
		if self.id != plugin_id:
			raise ValueError('Inconsistent plugin id, found {} in plugin_info.json but {} expected'.format(self.id, plugin_id))

		self.__dataset = _PluginDataSet.info
		self.__cache_manager = PluginRequestCacheManager(self, self.__request_cache_file)
		self.__cache_manager.load()

		self.__old_request_meta: Optional[RequestMeta] = None
		self.__new_request_meta: Optional[RequestMeta] = None

		self.__introduction_error: Dict[str, Exception] = {}
		self.__meta_info_error: Optional[Exception] = None
		self.__release_summary_error: Optional[Exception] = None
		self.__repository_info_error: Optional[Exception] = None

		self.__old_introduction: Dict[str, str] = {}
		self.__old_meta_info: Optional[MetaInfo] = None
		self.__old_release_summary: Optional[ReleaseSummary] = None
		self.__old_repository_info: Optional[RepositoryInfo] = None

	# ========================= property && getter =========================

	@property
	def id(self) -> str:
		return self.__plugin_info.id

	@property
	def repos(self) -> GithubRepository:
		return self.__plugin_info.repos

	@property
	def authors(self) -> List[Author]:
		return self.__plugin_info.authors

	@property
	def labels(self) -> List[Label]:
		return self.__plugin_info.labels

	@property
	def introduction(self) -> Text:
		return self.__introduction
	
	@property
	def plugin_info(self) -> _PluginInfoInternal:
		return self.__plugin_info

	def get_introduction_urls(self, kind: Literal['page', 'raw']) -> Dict[str, str]:
		def get_base_url(repos: GithubRepository) -> str:
			return repos.get_page_url_base() if kind == 'page' else repos.get_raw_url_base()

		if self.__plugin_info.external_introduction:
			return {
				lang: get_base_url(self.repos) + '/' + path
				for lang, path in self.__plugin_info.external_introduction.items()
			}
		else:	
			path = {}
			for lang in LANGUAGES:
				with with_language(lang):
					rel_path = (self.__info_directory / get_file_name('introduction.md')).relative_to(constants.REPOS_ROOT)
					path[lang] = get_base_url(PLUGIN_CATALOGUE) + '/' + rel_path.as_posix()
			return path

	@property
	def latest_version(self) -> str:
		if self.release_summary.latest_version is not None:
			return self.release_summary.latest_version
		return self.meta_info.version

	def is_disabled(self) -> bool:
		return self.__plugin_info.disable

	def get_disable_reason(self) -> str:
		return self.__plugin_info.disable_reason

	def is_data_fetched(self) -> bool:
		return self.__dataset.is_everything_fetched()

	def __repr__(self):
		return 'Plugin[id={},repository={}]'.format(self.id, self.repos.repos_url)

	# ========================= utils =========================

	async def get_repos_json(self, file_path: str, **kwargs) -> dict:
		resp = await self.repos.request_repos_file(file_path, **kwargs)
		if resp.status_code != 200:
			raise Exception('status code {} (should be 200) when fetching json {} from {}'.format(resp.status_code, file_path, resp.url))
		try:
			return resp.json()
		except JSONDecodeError:
			raise Exception('Failed to decode json from response! url: {}, status_code {}: {}'.format(resp.url, resp.status_code, resp.content)) from None

	async def get_repos_text(self, file_path: str, default: Optional[str] = None, **kwargs) -> str:
		resp = await self.repos.request_repos_file(file_path, **kwargs)
		if resp.status_code != 200:
			if default is not None:
				return default
			else:
				raise Exception('status code {} (should be 200) when fetching text {} from {}'.format(resp.status_code, file_path, resp.url))
		return resp.text

	def __read_old_file(self, path: Path, clazz: Type[_S], what: str) -> Optional[_S]:
		try:
			data = file_utils.load_json(path)
			return clazz.deserialize(data)
		except Exception as e:
			if not isinstance(e, FileNotFoundError):
				log.error('({}) read old {} failed: {}'.format(self.id, what, e))
			return None

	# ========================= File Index =========================

	@property
	def __request_meta_file(self) -> Path:
		return constants.META_FOLDER / self.id / '.request_meta.json'

	def load_old_request_meta(self):
		self.__old_request_meta = self.__read_old_file(self.__request_meta_file, RequestMeta, 'request meta')

	def reuse_old_fetch_results(self):
		def create_item(obj: Any, old_obj: Any, err: Optional[Exception], prev_getter: Callable[[], Optional[RequestMeta.Item]]) -> RequestMeta.Item:
			if obj is not None:
				return RequestMeta.Item(ttl=REQUEST_META_DEFAULT_TTL, last_failure=None)

			current_failure = '({}) {}'.format(type(err), err) if err is not None else None
			if old_obj is None:
				return RequestMeta.Item(ttl=0, last_failure=current_failure)

			# obj is None, old_obj is not None. Reuse old
			if self.__old_request_meta is None or (prev_item := prev_getter()) is None:
				# prev_item unavailable
				return RequestMeta.Item(ttl=REQUEST_META_DEFAULT_TTL - 1, last_failure=current_failure)
			else:
				rmi = RequestMeta.Item(ttl=max(0, prev_item.ttl - 1), last_failure=current_failure)
				if rmi.ttl > 0:  # obj is None, ttl > 0, will reuse
					rmi.created_at = prev_item.created_at
					rmi.created_by_github_action_id = prev_item.created_by_github_action_id
				return rmi

		introduction_items: Dict[str, RequestMeta.Item] = {}
		external_introduction_langs = [lang for lang in LANGUAGES if lang in self.__plugin_info.external_introduction]
		for lang in external_introduction_langs:
			intro_err = self.__introduction_error.get(lang)
			if (curr_text := self.__introduction.get_mapping().get(lang)) == self.__create_external_introduction_error_text(lang) or intro_err:
				curr_text = None
			if (prev_text := self.__old_introduction.get(lang)) == self.__create_external_introduction_error_text(lang):
				prev_text = None
			introduction_items[lang] = create_item(curr_text, prev_text, intro_err, lambda: self.__old_request_meta.introduction.get(lang))

		request_meta = RequestMeta(
			introduction=introduction_items,
			meta=create_item(self.meta_info, self.__old_meta_info, self.__meta_info_error, lambda: self.__old_request_meta.meta),
			release=create_item(self.release_summary, self.__old_release_summary, self.__release_summary_error, lambda: self.__old_request_meta.release),
			repository=create_item(self.repository_info, self.__old_repository_info, self.__repository_info_error, lambda: self.__old_request_meta.repository),
		)

		if self.__introduction is not None:  # should not be None after the `self.fetch_introduction()` call
			for lang in external_introduction_langs:
				if self.__introduction_error.get(lang) is not None and (imeta := request_meta.introduction[lang]).ttl > 0:
					if (old_intro := self.__old_introduction.get(lang)) is not None:
						log.info('({}) Reusing old external introduction for language {}, {!r}'.format(self.id, lang, imeta))
						self.__introduction.set(lang, old_intro)
		else:
			log.warning('({}) reuse_old_fetch_results() called before self.__introduction is set'.format(self.id))

		if self.meta_info is None and request_meta.meta.ttl > 0:
			log.info('({}) Reusing old meta_info, {!r}'.format(self.id, request_meta.meta))
			self.meta_info = self.__old_meta_info
		if self.release_summary is None and request_meta.release.ttl > 0:
			log.info('({}) Reusing old release_summary, {!r}'.format(self.id, request_meta.release))
			self.release_summary = self.__old_release_summary
		if self.repository_info is None and request_meta.repository.ttl > 0:
			log.info('({}) Reusing old repository_info, {!r}'.format(self.id, request_meta.repository))
			self.repository_info = self.__old_repository_info

		self.__new_request_meta = request_meta

	def save_request_meta(self):
		if self.__new_request_meta is None:
			raise RuntimeError('self.__new_request_meta is not initialized, please call `reuse_old_fetch_results` first')
		file_utils.save_json(self.__new_request_meta.serialize(), self.__request_meta_file)

	# ========================= Request Cache =========================

	@property
	def __request_cache_file(self) -> Path:
		return constants.META_FOLDER / self.id / '.request_cache.json'

	def save_request_cache(self):
		file_utils.save_json(self.__cache_manager.dump_for_save(), self.__request_cache_file)

	# ========================= Introduction =========================

	@classmethod
	@functools.lru_cache(None)
	def __create_external_introduction_error_text(cls, lang: str) -> str:
		with with_language(lang):
			return '*{}*'.format(Text('data_fetched_failed'))

	async def fetch_introduction(self):
		external_introduction = self.__plugin_info.external_introduction
		introduction_translations = {}
		for lang in LANGUAGES:
			with with_language(lang):
				file_location = external_introduction.get(lang)
				if file_location is not None:
					try:
						file_content = await self.get_repos_text(file_location)
					except Exception as e:
						log.exception('Failed to get custom introduction file in language {} from {} in {}'.format(lang, file_location, self))
						reporter.record_plugin_failure(self.id, 'Fetch custom introduction file in language {} from {} failed'.format(lang, file_location), e)
						introduction_translations[lang] = self.__create_external_introduction_error_text(lang)
						self.__introduction_error[lang] = e
					else:
						if file_location.lower().endswith('.md'):
							file_content = markdown_utils.rewrite_markdown(
								file_content,
								repos_url=self.repos.get_page_url_base(),
								raw_url=self.repos.get_raw_url_base(),
							)
						introduction_translations[lang] = file_content
				else:
					introduction_tr_file_path = self.__info_directory / get_file_name('introduction.md')
					if introduction_tr_file_path.is_file():
						with file_utils.open_for_read(introduction_tr_file_path) as file_handler:
							introduction_translations[lang] = file_handler.read()
		if not any(i for i in introduction_translations.values() if i):
			msg = 'No introduction file in any language found for {}'.format(self)
			log.warning(msg)
			reporter.record_warning(self.id, msg, FileNotFoundError('Neither external or internal introduction file found'))
		self.__introduction = BundledText(introduction_translations)
		self.__dataset |= _PluginDataSet.introduction
		log.info('({}) Introduction fetched'.format(self.id))

	def load_old_introduction(self):
		old_fpi = self.__read_old_file(self.__formatted_plugin_info_file, PluginInfo, 'PluginInfo')
		if old_fpi is not None:
			self.__old_introduction = old_fpi.introduction

	# ========================= PluginInfo =========================

	def generate_formatted_plugin_info(self) -> PluginInfo:
		if (_PluginDataSet.info | _PluginDataSet.introduction) not in self.__dataset:
			raise RuntimeError('not enough info. current dataset: {}'.format(self.__dataset))
		return PluginInfo(
			id=self.id,
			authors=[author.name for author in self.__plugin_info.authors],
			repository=self.repos.repos_url,
			branch=self.repos.branch,
			related_path=self.repos.related_path,
			labels=[label.id for label in self.__plugin_info.labels],
			introduction=self.__introduction.get_mapping().copy(),
			introduction_urls=self.get_introduction_urls(kind='raw'),
		)

	@property
	def __formatted_plugin_info_file(self) -> Path:
		return constants.META_FOLDER / self.id / 'plugin.json'

	def save_formatted_plugin_info(self):
		info = self.generate_formatted_plugin_info()
		file_utils.save_json(info.serialize(), self.__formatted_plugin_info_file)

	# ========================= MetaInfo =========================

	async def fetch_meta(self):
		try:
			self.meta_info = await MetaInfo.fetch_from_repos(self)
		except Exception as e:
			self.__meta_info_error = e
			raise
		else:
			self.__meta_info_error = None
		self.__dataset |= _PluginDataSet.meta
		log.info('({}) MetaInfo fetched'.format(self.id))

	@property
	def __meta_info_file(self) -> Path:
		return constants.META_FOLDER / self.id / 'meta.json'

	def load_old_meta_info(self):
		self.__old_meta_info = self.__read_old_file(self.__meta_info_file, MetaInfo, 'MetaInfo')

	def save_meta_info_if_available(self):
		if self.meta_info is not None:
			file_utils.save_json(self.meta_info.serialize(), self.__meta_info_file)
		else:
			log.warning('({}) Skipping saving meta_info due to error {}'.format(self.id, self.__meta_info_error))

	# ========================= Release & Cache =========================

	async def fetch_release(self):
		try:
			self.release_summary = await ReleaseSummary.create_for(self, self.__cache_manager)
		except Exception as e:
			self.__release_summary_error = e
			raise
		else:
			self.__release_summary_error = None
		self.__dataset |= _PluginDataSet.releases
		log.info('({}) Release fetched'.format(self.id))

	@property
	def __release_info_file(self) -> Path:
		return constants.META_FOLDER / self.id / 'release.json'

	def load_old_release_summary(self):
		self.__old_release_summary = self.__read_old_file(self.__release_info_file, ReleaseSummary, 'ReleaseSummary')

	def save_release_summary_if_available(self):
		if self.release_summary is not None:
			file_utils.save_json(self.release_summary.serialize(), self.__release_info_file)
		else:
			log.warning('({}) Skipping saving release_summary due to error {}'.format(self.id, self.__release_summary_error))

	# ========================= RepositoryInfo =========================

	async def fetch_and_update_repository(self):
		try:
			self.repository_info = await RepositoryInfo.create_for(self, self.__cache_manager)
		except Exception as e:
			self.__repository_info_error = e
			raise
		else:
			self.__repository_info_error = None

		self.repos.update_from_api(self.id, self.repository_info)
		self.__dataset |= _PluginDataSet.repository
		log.info('({}) Repository information fetched'.format(self.id))

	@property
	def __repository_info_file(self) -> Path:
		return constants.META_FOLDER / self.id / 'repository.json'

	def load_old_repository_info(self):
		self.__old_repository_info = self.__read_old_file(self.__repository_info_file, RepositoryInfo, 'RepositoryInfo')

	def save_repository_info_if_available(self):
		if self.repository_info is not None:
			file_utils.save_json(self.repository_info.serialize(), self.__repository_info_file)
		else:
			log.warning('({}) Skipping saving repository_info due to error {}'.format(self.id, self.__repository_info_error))

	# ========================= AllOfAPlugin =========================

	def create_and_save_all_data(self) -> AllOfAPlugin:
		if not self.meta_info:
			log.warning('({}) [create all] meta_info unavailable'.format(self.id))
		if not self.release_summary:
			log.warning('({}) [create all] release_summary unavailable'.format(self.id))
		if not self.repository_info:
			log.warning('({}) [create all] repository_info unavailable'.format(self.id))
		aop = AllOfAPlugin(
			meta=self.meta_info,
			plugin=self.generate_formatted_plugin_info(),
			release=self.release_summary,
			repository=self.repository_info,
		)
		file_utils.save_json(aop.serialize(), constants.META_FOLDER / self.id / 'all.json', with_gz=True)
		return aop


if __name__ == '__main__':
	Plugin('quick_backup_multi').fetch_meta()
