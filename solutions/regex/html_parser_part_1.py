from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lines = []

    def _add(self, label, tag, attrs=()):
        self.lines.append("{} : {}".format(label, tag))
        self.lines.extend("-> {} > {}".format(name, value) for name, value in attrs)

    def handle_starttag(self, tag, attrs):
        self._add("Start", tag, attrs)

    def handle_endtag(self, tag):
        self._add("End  ", tag)

    def handle_startendtag(self, tag, attrs):
        self._add("Empty", tag, attrs)


def parse(html):
    parser = MyHTMLParser()
    parser.feed(html)
    return parser.lines
