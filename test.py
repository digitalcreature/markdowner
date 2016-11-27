import markdowner
import re

html = markdowner.HTML()

html.\
	open("html").\
		open("head").\
			open("title").\
				content("test page").\
			close().\
		close().\
		open("body", style="color: red").\
			open("h1").\
				content("hello, world!").\
			close().\
			open("p").\
				content("here is some text").\
			close().\
		close().\
	close()
