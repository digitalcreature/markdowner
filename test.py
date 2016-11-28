import markdowner
import re

html = markdowner.HTML()

print(markdowner.HTML.opentag("code", id="sample1", language="c++"))
print(markdowner.HTML.closetag("code"))

html.\
	open("html").\
		open("head").\
			tag("title", "test page").\
		close().\
		open("body", style="color: red").\
			tag("h1", "hello, world!", id="hello").\
			open("p").\
				content("here is some text").\
				single("br").\
closeall()
