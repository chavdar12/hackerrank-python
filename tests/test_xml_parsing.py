import unittest
import xml.etree.ElementTree as etree

from solutions.xml_parsing.find_the_score import get_attr_number
from solutions.xml_parsing.maximum_depth import max_depth

FEED = """<feed xml:lang='en'>
    <title>HackerRank</title>
    <subtitle lang='en'>Programming challenges</subtitle>
    <link rel='alternate' type='text/html' href='http://hackerrank.com/'/>
    <updated>2013-12-25T12:00:00</updated>
    <entry>
        <author gender='male'>Harsh</author>
        <question type='hard'>XML 1</question>
        <description type='text'>This is related to XML parsing</description>
    </entry>
</feed>"""


class TestFindTheScore(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(get_attr_number(etree.fromstring(FEED)), 8)


class TestMaximumDepth(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(max_depth(etree.fromstring(FEED)), 2)

    def test_root_only(self):
        self.assertEqual(max_depth(etree.fromstring("<a/>")), 0)


if __name__ == "__main__":
    unittest.main()
