import argparse
import asyncio
from argparse import ArgumentParser
from typing import Collection, Optional

from catalogue.doc_gen import generate_doc
from common import log
from common.report import reporter
from plugin.plugin_list import get_plugin_list


async def check(target_ids: Optional[Collection[str]]):
	plugin_list = get_plugin_list(target_ids)
	# don't fetch release, so GitHub api token is not needed
	await plugin_list.fetch_data(no_api_token=True, fail_hard=True)


async def fetch_and_store_data(target_ids: Optional[Collection[str]]):
	plugin_list = get_plugin_list(target_ids)
	await plugin_list.fetch_data(fail_hard=False)
	plugin_list.store_data()


async def async_main(parser: argparse.ArgumentParser, args: argparse.Namespace):
	if args.targets == '':
		target_ids = None
	else:
		target_ids = args.targets.split(',')
		log.info('Targets: {}'.format(', '.join(target_ids)))

	reporter.record_command(args.subparser_name)
	reporter.record_script_start()

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
		await generate_doc(target_ids)
	else:
		parser.print_help()

	reporter.record_script_end()
	reporter.report(get_plugin_list())


def main():
	parser = ArgumentParser(prog='python manager', description='Plugin Catalogue Manager')
	parser.add_argument('--targets', default='', help='The target plugin ids to be processed, can be separated by "," just like csv format. By default all plugins will be processed')

	subparsers = parser.add_subparsers(title='Command', help='Available commands', dest='subparser_name')
	subparsers.add_parser('check', help='Check the correctness of files in "plugins/"')
	subparsers.add_parser('data', help='Fetch all needed data of plugins from github, and save to "meta/"')
	subparsers.add_parser('doc', help='Generate user friendly plugin catalogue doc to "catalogue/"')

	all_parser = subparsers.add_parser('all', help='Run everything above: check, fetch, doc')
	all_parser.add_argument('--no-check', action='store_true', help='Skip the check')

	args = parser.parse_args()
	asyncio.run(async_main(parser, args))


if __name__ == '__main__':
	main()
