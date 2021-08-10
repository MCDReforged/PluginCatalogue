from concurrent.futures.thread import ThreadPoolExecutor

from plugin import get_plugin_list


def main():
	plugin_list = get_plugin_list()
	print('Checking repository for {} plugins'.format(len(plugin_list)))
	with ThreadPoolExecutor(max_workers=16) as executor:
		for plugin in plugin_list:
			executor.submit(plugin.check_repository)


if __name__ == '__main__':
	main()
