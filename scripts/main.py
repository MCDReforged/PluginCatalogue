from argparse import ArgumentParser
from typing import Collection, Optional

import thread_pools
from doc_gen import generate_doc
from plugin_list import get_plugin_list
from report import reporter


def check(target_ids: Optional[Collection[str]]):
	get_plugin_list(target_ids).fetch_data(meta=True, release=False, fail_hard=True)  # so github api token is not needed


def update_data():
	plugin_list = get_plugin_list()
	plugin_list.fetch_data(fail_hard=False)
	plugin_list.store_data()


def main():
	parser = ArgumentParser(prog='python manager', description='Plugin Catalogue Manager')
	subparsers = parser.add_subparsers(title='Command', help='Available commands', dest='subparser_name')

	check_parser = subparsers.add_parser('check', help='Check the correctness of files in "plugins/"')
	check_parser.add_argument('--id', default='', help='The plugin id to be checked, can be separated by "," just like csv format. By default all plugins will be checked')

	subparsers.add_parser('fetch', help='Fetch metadata and release information from github to "meta/"')
	subparsers.add_parser('doc', help='Generate user friendly plugin catalogue doc to "catalogue/"')
	subparsers.add_parser('all', help='Run everything above: check, fetch, doc')

	args = parser.parse_args()
	reporter.record_command(args.subparser_name)
	if args.subparser_name == 'check':
		check(None if args.id == '' else args.id.split(','))
	elif args.subparser_name == 'fetch':
		update_data()
	elif args.subparser_name == 'doc':
		generate_doc()
	elif args.subparser_name == 'all':
		check(None)
		update_data()
		generate_doc()
	else:
		parser.print_help()

	reporter.report(get_plugin_list())
	thread_pools.shutdown()


if __name__ == '__main__':
	main()
