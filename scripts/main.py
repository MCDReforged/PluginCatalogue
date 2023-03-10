from argparse import ArgumentParser
from typing import Collection, Optional

import thread_pools
from doc_gen import generate_doc
from plugin_list import get_plugin_list
from report import reporter


def check(target_ids: Optional[Collection[str]]):
	get_plugin_list(target_ids).fetch_data(meta=True, release=False, fail_hard=True)  # so github api token is not needed


def update_data(target_ids: Optional[Collection[str]]):
	plugin_list = get_plugin_list(target_ids)
	plugin_list.fetch_data(fail_hard=False)
	plugin_list.store_data()


def main():
	parser = ArgumentParser(prog='python manager', description='Plugin Catalogue Manager')
	parser.add_argument('--targets', default='', help='The target plugin ids to be processed, can be separated by "," just like csv format. By default all plugins will be processed')

	subparsers = parser.add_subparsers(title='Command', help='Available commands', dest='subparser_name')
	subparsers.add_parser('check', help='Check the correctness of files in "plugins/"')
	subparsers.add_parser('fetch', help='Fetch metadata and release information from github to "meta/"')
	subparsers.add_parser('doc', help='Generate user friendly plugin catalogue doc to "catalogue/"')
	subparsers.add_parser('all', help='Run everything above: check, fetch, doc')

	args = parser.parse_args()
	if args.targets == '':
		target_ids = None
	else:
		target_ids = args.targets.split(',')
		print('Targets: {}'.format(', '.join(target_ids)))
	reporter.record_command(args.subparser_name)
	reporter.record_script_start()

	if args.subparser_name == 'check':
		check(target_ids)
	elif args.subparser_name == 'fetch':
		update_data(target_ids)
	elif args.subparser_name == 'doc':
		generate_doc(target_ids)
	elif args.subparser_name == 'all':
		check(target_ids)
		update_data(target_ids)
		generate_doc(target_ids)
	else:
		parser.print_help()

	reporter.record_script_end()
	reporter.report(get_plugin_list())
	thread_pools.shutdown()


if __name__ == '__main__':
	main()
