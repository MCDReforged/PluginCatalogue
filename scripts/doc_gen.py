import os
import re
import shutil
from contextlib import contextmanager
from typing import List, IO, Iterable

import constants
import utils
from label import get_label_set
from plugin import get_plugin_list, Plugin
from translation import Text, get_language, DEFAULT_LANGUAGE, LANGUAGES, with_language


def get_plugin_detail_link(plugin_id: str):
	return '/plugins/{}/{}'.format(plugin_id, get_file_name('readme.md'))


def get_label_doc_link(label_id: str):
	return '/labels/{}/{}'.format(label_id, get_file_name('readme.md'))


def get_file_name(name: str) -> str:
	base, extension = name.rsplit('.', 1)
	split = base.rsplit('-', 1)
	if len(split) == 2 and split[1] in LANGUAGES:
		base = split[0]
	if get_language() == DEFAULT_LANGUAGE:
		return '{}.{}'.format(base, extension)
	else:
		return '{}-{}.{}'.format(base, get_language(), extension)


def write_translation_nav(file_name: str, file: IO[str]):
	nav_list = []
	for lang in LANGUAGES:
		with with_language(lang):
			lang_name = Text('_language_name').get()
		if lang == get_language():
			text = '**{}**'.format(lang_name)
		else:
			with with_language(lang):
				text = '[{}]({})'.format(lang_name, get_file_name(file_name))
		nav_list.append('{}'.format(text))
	file.write('{}\n'.format(' | '.join(nav_list)))
	file.write('\n')


@contextmanager
def write_file_with_translation_nav(file_path: str):
	with utils.write_file(file_path) as file:
		write_translation_nav(os.path.basename(file_path), file)
		yield file


def write_label_info(file: IO[str]):
	label_set = get_label_set()
	file.write('## {}\n'.format(Text('label_index')))
	file.write('\n')
	for label in label_set.get_label_list():
		file.write('- [{}]({})\n'.format(label, get_label_doc_link(label.id)))
	file.write('\n')


def generate_index(plugin_list: Iterable[Plugin], file: IO[str]):
	plugin_list = list(plugin_list)
	file.write('{}: {}\n'.format(Text('plugin_amount'), len(plugin_list)))
	file.write('\n')
	file.write('| {} | {} | {} | {} |\n'.format(Text('plugin_name'), Text('version'), Text('authors'), Text('labels')))
	file.write('| --- | --- | --- | --- |\n')
	for plugin in plugin_list:
		file.write('| [{}]({}) | {} | {} | {} |\n'.format(
			plugin.name, get_plugin_detail_link(plugin.id),
			plugin.latest_version,
			', '.join(map(lambda a: a.to_markdown(), plugin.authors)),
			', '.join(map(lambda l: '[{}]({})'.format(l, get_label_doc_link(l.id)), plugin.labels))
		))


def write_plugin(plugin: Plugin, file: IO[str]):
	file.write('## {}\n'.format(plugin.id))
	file.write('\n')
	file.write('- {}: `{}`\n'.format(Text('plugin_id'), plugin.id))
	file.write('- {}: {}\n'.format(Text('plugin_name'), plugin.name))
	file.write('- {}: {}\n'.format(Text('version'), plugin.latest_version))
	file.write('  - {}: {}\n'.format(Text('metadata_version'), plugin.meta_info.version))
	file.write('  - {}: {}\n'.format(Text('release_version'), plugin.release_summary.latest_version))
	file.write('- {}: {}\n'.format(Text('authors'), ', '.join(map(lambda a: a.to_markdown(), plugin.authors))))
	file.write('- {}: {}\n'.format(Text('repository'), plugin.repository))
	file.write('- {}: {}\n'.format(Text('labels'), ', '.join(map(lambda l: '`{}`'.format(l), plugin.labels))))
	if len(plugin.meta_info.dependencies) > 0:
		file.write('- {}:\n'.format(Text('dependencies')))
		file.write('\n')
		file.write('| {} | {} |\n'.format(Text('plugin_id'), Text('dependencies.requirement')))
		file.write('| --- | --- |\n')
		for pid, req in plugin.meta_info.dependencies.items():
			file.write('| [{}]({}) | {} |\n'.format(pid, get_plugin_detail_link(pid), utils.format_markdown(req)))
		file.write('\n')
	else:
		file.write('- {}: {}\n'.format(Text('dependencies'), Text('none')))
	if len(plugin.meta_info.requirements) > 0:
		file.write('- {}:\n'.format(Text('requirements')))
		file.write('\n')
		file.write('| {} | {} |\n'.format(Text('python_package'), Text('requirements.requirement')))
		file.write('| --- | --- |\n')
		for line in plugin.meta_info.requirements:
			package = re.match(r'^[A-Za-z.-]+', line).group()
			req = utils.remove_prefix(line, package)
			file.write('| [{}](https://pypi.org/project/{}/) | {} |\n'.format(
				package, package,
				utils.format_markdown(req)
			))
		file.write('\n')
	else:
		file.write('- {}: {}\n'.format(Text('requirements'), Text('none')))
	file.write('\n')
	file.write('**{}**\n'.format(Text('description')))
	file.write('\n')
	file.write(plugin.readme.get())
	file.write('\n')


def generate_full(plugin_list: Iterable[Plugin], file: IO[str]):
	with utils.read_file(os.path.join(constants.TEMPLATE_FOLDER, get_file_name('full_header.md'))) as header:
		file.write(header.read())
	file.write('\n')
	for plugin in plugin_list:
		write_plugin(plugin, file)


def generate_labels(plugin_list: List[Plugin]):
	label_root = os.path.join(constants.CATALOGUE_FOLDER, 'labels')
	for label in get_label_set().get_label_list():
		with write_file_with_translation_nav(os.path.join(label_root, label.id, get_file_name('readme.md'))) as file:
			file.write('# {}\n'.format(label))
			file.write('\n')
			file.write('{}\n'.format(Text('plugin_index_with_label')).format(label))
			file.write('\n')
			generate_index(filter(lambda plg: label in plg.labels, plugin_list), file)


def generate_plugins(plugin_list: List[Plugin]):
	plugin_root = os.path.join(constants.CATALOGUE_FOLDER, 'plugins')
	for plugin in plugin_list:
		with write_file_with_translation_nav(os.path.join(plugin_root, plugin.id, get_file_name('readme.md'))) as file:
			write_plugin(plugin, file)


def generate_doc():
	print('Generating doc')
	plugin_list = get_plugin_list()
	plugin_list.fetch_data(fail_hard=False)
	if os.path.isdir(constants.CATALOGUE_FOLDER):
		shutil.rmtree(constants.CATALOGUE_FOLDER)
	os.mkdir(constants.CATALOGUE_FOLDER)

	def write_doc():
		with write_file_with_translation_nav(os.path.join(constants.CATALOGUE_FOLDER, get_file_name('readme.md'))) as file:
			with utils.read_file(os.path.join(constants.TEMPLATE_FOLDER, get_file_name('index_header.md'))) as header:
				file.write(header.read())
			file.write('\n')
			write_label_info(file)
			file.write('-------\n\n')
			generate_index(plugin_list, file)

		generate_labels(plugin_list)
		generate_plugins(plugin_list)

		with write_file_with_translation_nav(os.path.join(constants.CATALOGUE_FOLDER, get_file_name('full.md'))) as file:
			generate_full(plugin_list, file)

	for lang in LANGUAGES:
		print('Generating doc in language {}'.format(lang))
		with with_language(lang):
			write_doc()

