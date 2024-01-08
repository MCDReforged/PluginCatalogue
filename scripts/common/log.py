import logging
import sys
import threading

__all__ = [
	'logger',
	'debug', 'info', 'warning', 'error', 'exception',
]


def __setup_logger():
	class Handler(logging.StreamHandler):
		def __init__(self):
			super().__init__(stream=sys.stdout)
			self.__lock = threading.Lock()
			self.setFormatter(logging.Formatter('[%(levelname_short)s] %(message)s'))

		def emit(self, record):
			record.levelname_short = {
				logging.WARNING: 'WARN',
			}.get(record.levelno, record.levelname)[:5].ljust(5, ' ').upper()
			with self.__lock:
				super().emit(record)

	logger.setLevel(logging.DEBUG)
	logger.addHandler(Handler())


logger = logging.Logger('manager')
__setup_logger()

debug = logger.debug
info = logger.info
warning = logger.warning
error = logger.error
exception = logger.exception
