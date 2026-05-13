import argparse
import asyncio
import traceback
from argparse import ArgumentParser
from typing import Collection, Optional

from catalogue.doc_gen import generate_doc
from common import constants, log
from common.report import reporter
from plugin.plugin_list import get_plugin_list
from utils import file_utils


async def check(target_ids: Optional[Collection[str]]):
	plugin_list = get_plugin_list(target_ids)
	await plugin_list.fetch_data(fail_hard=True, skip_release=True)


async def fetch_and_store_data(target_ids: Optional[Collection[str]]):
	plugin_list = get_plugin_list(target_ids)
	await plugin_list.fetch_data(fail_hard=False, reuse_old_on_failures=True)
	plugin_list.store_data()


def auto_disable_failed_plugins():
	for plugin_id, failures in reporter.failures.items():
		if len(failures) == 0:
			continue

		plugin_info_path = constants.PLUGINS_FOLDER / plugin_id / 'plugin_info.json'
		try:
			plugin_info = file_utils.load_json(plugin_info_path)
		except FileNotFoundError:
			log.warning('Skipping auto disable for plugin {}, plugin_info.json not found'.format(plugin_id))
			continue
		except Exception:
			log.exception('Cannot auto disable plugin {}, failed to load plugin_info.json'.format(plugin_id))
			continue

		if plugin_info.get('disable'):
			continue

		first_failure = failures[0] if len(failures) > 0 else 'unknown failure'
		reason = 'Auto disabled by scheduled update ({} failures): {}'.format(len(failures), first_failure)
		plugin_info['disable'] = True
		plugin_info['disable_reason'] = reason
		file_utils.save_json(plugin_info, plugin_info_path)
		reporter.record_plugin_disabled(plugin_id, reason)
		log.warning('Auto disabled plugin {} due to fetch failures'.format(plugin_id))


async def async_main(parser: argparse.ArgumentParser, args: argparse.Namespace):
	if args.targets == '':
		target_ids = None
	else:
		target_ids = args.targets.split(',')
		log.info('Targets: {}'.format(', '.join(target_ids)))

	reporter.record_command(args.subparser_name)
	reporter.record_script_start()

	try:
		if args.subparser_name == 'check':
			await check(target_ids)
		elif args.subparser_name == 'data':
			await fetch_and_store_data(target_ids)
		elif args.subparser_name == 'doc':
			await generate_doc(target_ids)
		elif args.subparser_name == 'all':
			if not args.no_check:
				await check(target_ids)
			await fetch_and_store_data(target_ids)
			if args.auto_disable_failures:
				auto_disable_failed_plugins()
			await generate_doc(target_ids)
		else:
			parser.print_help()
	except Exception as e:
		reporter.record_script_failure(e, traceback.format_exc())
		raise
	finally:
		reporter.record_script_end()
		reporter.report(get_plugin_list())

		from utils.request_utils import RequestClientSessionHolder
		await RequestClientSessionHolder.get().shutdown()


def main():
	parser = ArgumentParser(prog='python manager', description='Plugin Catalogue Manager')
	parser.add_argument('--targets', default='', help='The target plugin ids to be processed, can be separated by "," just like csv format. By default all plugins will be processed')

	subparsers = parser.add_subparsers(title='Command', help='Available commands', dest='subparser_name')
	subparsers.add_parser('check', help='Check the correctness of files in "plugins/"')
	subparsers.add_parser('data', help='Fetch all needed data of plugins from github, and save to "meta/"')
	subparsers.add_parser('doc', help='Generate user friendly plugin catalogue doc to "catalogue/"')

	all_parser = subparsers.add_parser('all', help='Run everything above: check, fetch, doc')
	all_parser.add_argument('--no-check', action='store_true', help='Skip the check')
	all_parser.add_argument('--auto-disable-failures', action='store_true', help='Auto disable failed plugins by setting disable fields in plugin_info.json')

	args = parser.parse_args()
	asyncio.run(async_main(parser, args))


if __name__ == '__main__':
	main()
