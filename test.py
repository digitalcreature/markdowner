import markdowner
import re

html = markdowner.HTML()

html.\
	open("html").\
		open("head").\
			tag("title", "test page").\
		close().\
		open("body", style="color: red").\
			tag("h1", "hello, world!", id="hello").\
			open("p").\
				content("here is some text").\
			close().\
		close().\
	close()
