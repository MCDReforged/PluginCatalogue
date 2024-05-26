import os
import re
import shutil
import time
from contextlib import contextmanager
from typing import List, IO, Iterable, Any, Optional, Collection

from common import constants, log
from common.translation import Text, get_language, get_file_name, LANGUAGES, with_language
from plugin.label import get_label_set
from plugin.plugin import Plugin
from plugin.plugin_list import get_plugin_list
from utils import file_utils, value_utils, markdown_utils


def get_plugin_detail_link(plugin_id: str):
	if plugin_id == 'mcdreforged':
		return constants.MCDR_LINK
	else:
		return '/plugins/{}/{}'.format(plugin_id, get_file_name('readme.md'))


def get_label_doc_link(label_id: str):
	return '/labels/{}/{}'.format(label_id, get_file_name('readme.md'))


def failed() -> str:
	return '*{}*'.format(Text('data_fetched_failed'))


def none() -> str:
	return '*{}*'.format(Text('none'))


def formatted_time(created_at: str, precision: str) -> str:
	"""
	:param created_at: The created_at field from github api
	:param precision: should be 'day' or 'second'
	"""
	st = time.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ')
	fmt = '%Y/%m/%d'
	if precision == 'second':
		fmt += ' %H:%M:%S'
	return time.strftime(fmt, st)


def get_root_readme_file_path():
	return os.path.join(constants.CATALOGUE_FOLDER, get_file_name('readme.md'))


def get_full_index_file_path():
	return os.path.join(constants.CATALOGUE_FOLDER, get_file_name('full.md'))


def get_label_list_markdown(plugin: Plugin):
	return ', '.join(map(lambda label: '[`{}`]({})'.format(label, get_label_doc_link(label.id)), plugin.labels))


def write_translation_nav(file_name: str, file: IO[str]):
	nav_list = []
	for lang in LANGUAGES:
		with with_language(lang):
			lang_name = Text('_language_name').get()
		if lang == get_language():
			text = '**{}**'.format(lang_name)
		else:
			with with_language(lang):
				text = Link(lang_name, get_file_name(file_name))
		nav_list.append('{}'.format(text))
	file.write('{}\n'.format(' | '.join(nav_list)))
	file.write('\n')


def write_back_to_index_nav(file: IO[str]):
	file.write('{} {}\n'.format(markdown_utils.format_markdown('>>>'), Link(Text('back_to_index'), get_file_name('/readme.md'))))
	file.write('\n')


@contextmanager
def write_nav(file_path: str):
	with file_utils.open_for_write(file_path) as file:
		write_translation_nav(os.path.basename(file_path), file)
		if file_path != get_root_readme_file_path():
			write_back_to_index_nav(file)
		yield file


def write_label_info(file: IO[str]):
	label_set = get_label_set()
	file.write('## {}\n'.format(Text('label_index')))
	file.write('\n')
	for label in label_set.get_label_list():
		file.write('- {}\n'.format(Link(label, get_label_doc_link(label.id))))
	file.write('\n')


def generate_index(plugin_list: Iterable[Plugin], file: IO[str]):
	plugin_list = list(plugin_list)
	file.write('{}: {}\n'.format(Text('plugin_amount'), len(plugin_list)))
	file.write('\n')
	table = Table(Text('plugin_name'), Text('authors'), Text('description'), Text('last_update'), Text('labels'))
	for plugin in plugin_list:
		try:
			if plugin.is_data_fetched():
				name = plugin.meta_info.name
				translated_description = plugin.meta_info.translated_description
			else:
				name = translated_description = failed()
			release = plugin.release_summary.get_latest_release()
			if release is not None:
				last_update = formatted_time(release.created_at, precision='day')
			else:
				last_update = 'N/A'
			table.add_row(
				Link(name, get_plugin_detail_link(plugin.id)),
				', '.join(map(lambda a: a.to_markdown(), plugin.authors)),
				translated_description,
				last_update,
				get_label_list_markdown(plugin)
			)
		except:
			log.error('Failed to write plugin index of {}'.format(plugin))
			raise
	table.write(file)


def write_plugin_download(plugin: Plugin, file: IO[str], limit: int = 3):
	try:
		_write_plugin_download(plugin, file, limit)
	except:
		log.error('Failed to write plugin downloads of {}'.format(plugin))
		raise


def _write_plugin_download(plugin: Plugin, file: IO[str], limit: int):
	file.write('### {}\n'.format(Text('download')))
	file.write('\n')
	file.write('> [!IMPORTANT]\n')
	file.write('> {}\n'.format(Text('rtfm_warn')))
	file.write('\n')

	if plugin.release_summary is not None:
		table = Table(Text('file'), Text('version'), Text('upload_time'), Text('size'), Text('download_amount'), Text('operations'))
		for release in plugin.release_summary.releases:
			asset = release.asset
			table.add_row(
				Link(asset.name, release.url),
				release.meta.version,
				formatted_time(asset.created_at, precision='second'),
				value_utils.pretty_file_size(asset.size),
				asset.download_count,
				' '.join(map(str, [
					Link(Text('operations.download'), asset.browser_download_url)
				]))
			)
			if table.row_count == limit:
				break
		table.write(file)
	else:
		file.write('*{}*\n'.format(Text('data_fetched_failed')))
		file.write('\n')


def write_plugin(plugin: Plugin, file: IO[str]):
	try:
		_write_plugin(plugin, file)
	except:
		log.error('Failed to write plugin information of {}'.format(plugin))
		raise


def _write_plugin(plugin: Plugin, file: IO[str]):
	file.write('## {}\n'.format(plugin.id))
	file.write('\n')

	file.write('### {}\n'.format(Text('basic_info')))
	file.write('\n')

	file.write('- {}: `{}`\n'.format(Text('plugin_id'), plugin.id))
	if plugin.is_data_fetched():
		file.write('- {}: {}\n'.format(Text('plugin_name'), plugin.meta_info.name))
		file.write('- {}: {}\n'.format(Text('version'), plugin.latest_version))
		file.write('  - {}: {}\n'.format(Text('metadata_version'), plugin.meta_info.version))
		file.write('  - {}: {}\n'.format(Text('release_version'), plugin.release_summary.latest_version or 'N/A'))
	else:
		file.write('- {}: {}\n'.format(Text('version'), failed()))

	file.write('- {}: {}\n'.format(Text('total_downloads'), plugin.release_summary.get_total_downloads()))
	file.write('- {}: {}\n'.format(Text('authors'), ', '.join(map(lambda a: a.to_markdown(), plugin.authors))))
	file.write('- {}: {}\n'.format(Text('repository'), plugin.repos.repos_url))
	file.write('- {}: {}\n'.format(Text('repository_plugin_page'), plugin.repos.plugin_homepage))
	file.write('- {}: {}\n'.format(Text('labels'), get_label_list_markdown(plugin)))
	if plugin.is_data_fetched():
		file.write('- {}: {}\n'.format(Text('description'), plugin.meta_info.translated_description))
	else:
		file.write('- {}: {}\n'.format(Text('description'), failed()))
	file.write('\n')

	file.write('### {}\n'.format(Text('dependencies')))
	file.write('\n')
	if plugin.is_data_fetched():
		table = Table(Text('plugin_id'), Text('dependencies.requirement'))
		for pid, req in plugin.meta_info.dependencies.items():
			table.add_row(
				Link(pid, get_plugin_detail_link(pid)),
				markdown_utils.format_markdown(req)
			)
		table.write(file)
	else:
		file.write('{}\n'.format(failed()))
		file.write('\n')

	file.write('### {}\n'.format(Text('requirements')))
	file.write('\n')
	if plugin.is_data_fetched():
		table = Table(Text('python_package'), Text('requirements.requirement'))
		pip_reqs = []
		for line in plugin.meta_info.requirements:
			matched = re.match(r'^[^<>=~^]+', line)
			if matched is None:
				log.warning('Unknown requirement line "{}" in plugin {}'.format(line, plugin))
				continue
			pip_reqs.append(line)
			package = matched.group()
			req = value_utils.remove_prefix(line, package)
			table.add_row(
				Link(package, 'https://pypi.org/project/{}'.format(package)),
				markdown_utils.format_markdown(req)
			)
		table.write(file)

		if len(pip_reqs) > 0:
			def simple_quote(s: str) -> str:
				if re.fullmatch(r'[a-z0-9.~^=_-]+', s, re.ASCII | re.IGNORECASE):
					return s
				return '"' + s.replace('"', '\\"') + '"'

			file.write('```\n')
			file.write('{}\n'.format(' '.join(['pip', 'install', *map(simple_quote, pip_reqs)])))
			file.write('```\n\n')
	else:
		file.write('{}\n'.format(failed()))
		file.write('\n')

	file.write('### {}\n'.format(Text('introduction')))
	file.write('\n')
	file.write(plugin.introduction.get() or '{}\n'.format(none()))
	file.write('\n')


def generate_full(plugin_list: Iterable[Plugin], file: IO[str]):
	with file_utils.open_for_read(os.path.join(constants.TEMPLATE_FOLDER, get_file_name('full_header.md'))) as header:
		file.write(header.read())
	file.write('\n')
	for plugin in plugin_list:
		write_plugin(plugin, file)
		write_plugin_download(plugin, file)


def generate_labels(plugin_list: List[Plugin]):
	label_root = os.path.join(constants.CATALOGUE_FOLDER, 'labels')
	for label in get_label_set().get_label_list():
		with write_nav(os.path.join(label_root, label.id, get_file_name('readme.md'))) as file:
			file.write('# {}\n'.format(label))
			file.write('\n')
			file.write('{}\n'.format(Text('plugin_index_with_label')).format(label))
			file.write('\n')
			generate_index(filter(lambda plg: label in plg.labels, plugin_list), file)


def generate_plugins(plugin_list: List[Plugin]):
	plugin_root = os.path.join(constants.CATALOGUE_FOLDER, 'plugins')
	for plugin in plugin_list:
		with write_nav(os.path.join(plugin_root, plugin.id, get_file_name('readme.md'))) as file:
			write_plugin(plugin, file)
			write_plugin_download(plugin, file, limit=-1)


async def generate_doc(target_ids: Optional[Collection[str]] = None):
	log.info('Generating doc')
	plugin_list = get_plugin_list(target_ids)
	await plugin_list.fetch_data(fail_hard=False)
	if os.path.isdir(constants.CATALOGUE_FOLDER):
		shutil.rmtree(constants.CATALOGUE_FOLDER)
	os.mkdir(constants.CATALOGUE_FOLDER)

	def write_doc():
		with write_nav(get_root_readme_file_path()) as file:
			with file_utils.open_for_read(os.path.join(constants.TEMPLATE_FOLDER, get_file_name('index_header.md'))) as header:
				file.write(header.read())
			file.write('\n')
			write_label_info(file)
			file.write('-------\n\n')
			generate_index(plugin_list, file)

		generate_labels(plugin_list)
		generate_plugins(plugin_list)

		with write_nav(get_full_index_file_path()) as file:
			generate_full(plugin_list, file)

	for lang in LANGUAGES:
		log.info('Generating doc in language {}'.format(lang))
		with with_language(lang):
			write_doc()

	log.info('Generating doc done')


class Link:
	def __init__(self, display: Any, url: str):
		self.__display = str(display)
		self.__url = url

	def __str__(self):
		return '[{}]({})'.format(self.__display, self.__url)


class Table:
	def __init__(self, *title):
		self.__title = tuple(map(str, title))
		self.__rows: List[tuple] = []

	@property
	def row_count(self) -> int:
		return len(self.__rows)

	@property
	def column_count(self) -> int:
		return len(self.__title)

	def add_row(self, *items):
		assert len(items) == self.column_count, 'expected row width {}, but found row with width {}'.format(self.column_count, len(items))
		try:
			self.__rows.append(tuple(map(str, items)))
		except:
			log.error('Failed to add new rows to table, rows: {}'.format(items))
			raise

	@staticmethod
	def __write_row(file: IO[str], items: tuple):
		file.write('| {} |\n'.format(' | '.join(map(str, items))))

	def write(self, file: IO[str]):
		self.__write_row(file, self.__title)
		self.__write_row(file, ('---',) * self.column_count)
		for row in self.__rows:
			self.__write_row(file, row)
		file.write('\n')
