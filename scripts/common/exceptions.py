class CatalogueError(Exception):
	pass


class UnexpectedResponseStatusError(CatalogueError):
	def __init__(self, *, url: str, status_code: int, expected: str, content: bytes):
		self.url = url
		self.status_code = status_code
		self.expected = expected
		self.content = content
		super().__init__('unexpected status code {} (expected {}) for {}'.format(status_code, expected, url))


class ResponseJsonDecodeError(CatalogueError):
	def __init__(self, *, url: str, status_code: int, content: bytes):
		self.url = url
		self.status_code = status_code
		self.content = content
		super().__init__('failed to decode json from response for {} (status code {})'.format(url, status_code))


class AssetDownloadError(CatalogueError):
	def __init__(self, *, download_url: str, status_code: int, content: bytes):
		self.download_url = download_url
		self.status_code = status_code
		self.content = content
		super().__init__('download asset from {} failed with status code {}'.format(download_url, status_code))
