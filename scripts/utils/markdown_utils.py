import re
import threading

import mistletoe

from common import log


def format_markdown(text: str) -> str:
	for c in ('\\', '<', '>'):
		text = text.replace(c, '\\' + c)
	return text


# https://github.com/miyuchina/mistletoe/issues/210
__rewrite_markdown_lock = threading.Lock()


def rewrite_markdown(content: str, repos_url: str, raw_url: str) -> str:
	"""
	Example
	- repos: https://github.com/my/repos/, branch: master, file to rewrite: foobar/example.md
	- repos_url (for text files online view): https://github.com/my/repos/tree/master/foobar/
	- raw_url (for raw contents direct link): https://raw.githubusercontent.com/my/repos/master/foobar/
	"""
	from mistletoe.markdown_renderer import MarkdownRenderer
	from mistletoe.span_token import Image, Link

	repos_url = repos_url.rstrip('/')
	raw_url = raw_url.rstrip('/')
	content = content.replace('\r\n', '\n')
	pattern = re.compile(r'^\w+://', re.ASCII)

	def rewrite_url(url: str, rewrite_base: str) -> str:
		if not pattern.match(url):  # relative path
			if url in ['', '.'] or url.startswith('#'):
				pass  # keep untouched
			else:
				new_url = rewrite_base + '/' + url
				log.info('URL rewritten based on {!r}: {!r} -> {!r}'.format(rewrite_base, url, new_url))
				return new_url
		return url

	def rewrite_children(node):
		if isinstance(node, Image):
			node.src = rewrite_url(node.src, raw_url)
		elif isinstance(node, Link):
			node.target = rewrite_url(node.target, repos_url)

		children = getattr(node, 'children', [])
		for child in children:
			rewrite_children(child)

	with __rewrite_markdown_lock:
		with MarkdownRenderer() as renderer:
			doc = mistletoe.Document(content)
			rewrite_children(doc)
			return renderer.render(doc)


if __name__ == '__main__':
	print(rewrite_markdown(
		'abc\n\nfoobar ![asd](1.png)\n\n![bsd](2.md)\n\n![xxx](https://axsx.aaxx/x.txt)\n\n## 12',
		'https://example.com/repos',
		'https://example.com/raw',
	))
