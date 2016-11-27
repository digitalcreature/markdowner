import re

class Markdown:
	class _patterns:
		h = re.compile(r'(#{1,6})\s(.+)')
	def __init__(self):
		pass
	def render(self, md):
		return md
