
class HTML:

	def __init__(self):
		self.stack = []

	def indent(self, offset = 0):
		return "".ljust((len(self.stack) - 1) + offset, "\t")

	def open(self, tag, **attributes):
		self.stack.append(tag)
		str = "<%s" % tag
		for k in attributes:
			if attributes[k] != None:
				str = "%s %s = %r" % (str, k, attributes[k])
		str = "%s>" % str
		print("%s%s" % (self.indent(), str))
		return self
	def content(self, content):
		print("%s%s" % (self.indent(1),content))
		return self
	def close(self):
		print("%s</%s>" % (self.indent(), self.stack.pop()))
		return self
