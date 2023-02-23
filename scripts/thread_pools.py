from concurrent.futures import ThreadPoolExecutor

import constants

worker_pool = ThreadPoolExecutor(max_workers=constants.THREAD_POOL_WORKER, thread_name_prefix='worker')
downloader_pool = ThreadPoolExecutor(max_workers=constants.THREAD_POOL_WORKER, thread_name_prefix='downloader')


def shutdown():
	worker_pool.shutdown()
	downloader_pool.shutdown()
