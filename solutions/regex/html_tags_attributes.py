from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lines = []

    def handle_starttag(self, tag, attrs):
        self.lines.append(tag)
        self.lines.extend("-> {} > {}".format(name, value) for name, value in attrs)


def parse(html):
    parser = MyHTMLParser()
    parser.feed(html)
    return parser.lines
