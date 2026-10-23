from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lines = []

    def handle_comment(self, data):
        kind = "Multi-line" if "\n" in data else "Single-line"
        self.lines += [">>> {} Comment".format(kind), data]

    def handle_data(self, data):
        if data != "\n":
            self.lines += [">>> Data", data]


def parse(html):
    parser = MyHTMLParser()
    parser.feed(html)
    return parser.lines
