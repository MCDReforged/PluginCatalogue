from argparse import ArgumentParser

from doc_gen import generate_doc
from plugin_list import get_plugin_list


def check():
	get_plugin_list().fetch_data(meta=True, release=False, fail_hard=True)  # so github api token is not needed


def update_data():
	plugin_list = get_plugin_list()
	plugin_list.fetch_data(fail_hard=False)
	plugin_list.store_data()


def main():
	parser = ArgumentParser(prog='python manager', description='Plugin Catalogue Manager')
	subparsers = parser.add_subparsers(title='Command', help='Available commands', dest='subparser_name')

	subparsers.add_parser('check', help='Check the correctness of files in "plugins/"')
	subparsers.add_parser('fetch', help='Fetch metadata and release information from github to "meta/"')
	subparsers.add_parser('doc', help='Generate user friendly plugin catalogue doc to "catalogue/"')
	subparsers.add_parser('all', help='Run everything above')

	result = parser.parse_args()
	if result.subparser_name == 'check':
		check()
	elif result.subparser_name == 'fetch':
		update_data()
	elif result.subparser_name == 'doc':
		generate_doc()
	elif result.subparser_name == 'all':
		check()
		update_data()
		generate_doc()
	else:
		parser.print_help()


if __name__ == '__main__':
	main()
