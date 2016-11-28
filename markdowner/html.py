
class HTML:

	def __init__(self):
		self.stack = []

	def indent(self, offset = 0):
		return "".ljust((len(self.stack) - 1) + offset, "\t")

	def open(self, tag, **attributes):
		self.stack.append(tag)
		return self.single(tag, **attributes)
	def single(self, tag, **attributes):
		s = self.opentag(tag, **attributes)
		print("%s%s" % (self.indent(), s))
		return self
	def content(self, content):
		print("%s%s" % (self.indent(1),content))
		return self
	def close(self):
		print("%s%s" % (self.indent(), self.closetag(self.stack.pop())))
		return self
	def closeall(self):
		while len(self.stack) > 0:
			self.close()
	def tag(self, tag, content="", **attributes):
		return self.open(tag, **attributes).content(content).close()
	@staticmethod
	def opentag(tag, **attributes):
		s = "<%s" % tag
		for k in attributes:
			if attributes[k] != None:
				s = "%s %s = %r" % (s, k, str(attributes[k]))
		s = "%s>" % s
		return s
	@staticmethod
	def closetag(tag):
		return "</%s>" % tag
