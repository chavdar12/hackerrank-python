import unittest

from solutions.regex import html_parser_part_1, html_parser_part_2, html_tags_attributes
from solutions.regex.credit_card_numbers import is_valid_card
from solutions.regex.findall_finditer import vowel_runs
from solutions.regex.floating_point_number import is_float
from solutions.regex.group_groups_groupdict import first_repeating
from solutions.regex.hex_color_code import hex_colors
from solutions.regex.matrix_script import decode
from solutions.regex.parsing_email_addresses import valid_named_emails
from solutions.regex.phone_numbers import is_valid_phone
from solutions.regex.postal_codes import is_valid_postal_code
from solutions.regex.re_split import split_number
from solutions.regex.regex_substitution import sub_func
from solutions.regex.roman_numerals import is_roman
from solutions.regex.start_end import match_spans
from solutions.regex.uid import is_valid_uid


class TestFloatingPointNumber(unittest.TestCase):
    def test_sample(self):
        self.assertFalse(is_float("4.0O0"))
        self.assertTrue(is_float("-1.00"))
        self.assertTrue(is_float("+4.54"))
        self.assertFalse(is_float("SomeRandomStuff"))
        self.assertFalse(is_float("1."))


class TestReSplit(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(split_number("100,000,000.000"), ["100", "000", "000", "000"])


class TestGroupGroupsGroupdict(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(first_repeating("..12345678910111213141516171820212223"), "1")

    def test_none(self):
        self.assertEqual(first_repeating("abc"), -1)

    def test_ignores_symbols(self):
        self.assertEqual(first_repeating("__aa"), "a")


class TestFindallFinditer(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(vowel_runs("rabcdeefgyYhFjkIoomnpOeorteeeeet"), ["ee", "Ioo", "Oeo", "eeeee"])

    def test_none(self):
        self.assertEqual(vowel_runs("abc"), [-1])

    def test_needs_consonant_not_symbol(self):
        self.assertEqual(vowel_runs("+aa+"), [-1])


class TestStartEnd(unittest.TestCase):
    def test_overlapping(self):
        self.assertEqual(match_spans("aaadaa", "aa"), [(0, 1), (1, 2), (4, 5)])

    def test_none(self):
        self.assertEqual(match_spans("abc", "z"), [(-1, -1)])


class TestRegexSubstitution(unittest.TestCase):
    def test_sample(self):
        self.assertEqual(sub_func("if a + b > 0 && a - b < 0:"), "if a + b > 0 and a - b < 0:")
        self.assertEqual(sub_func("x&&&& && && &&& || ||| |||| || x"), "x&&&& and and &&& or ||| |||| or x")


class TestRomanNumerals(unittest.TestCase):
    def test_valid(self):
        for s in ("CDXXI", "MCMXCIV", "MMMCMXCIX", "IV", "XL"):
            self.assertTrue(is_roman(s), s)

    def test_invalid(self):
        for s in ("MMMM", "IIII", "XCX", "IL", "VX", ""):
            self.assertFalse(is_roman(s), s)


class TestPhoneNumbers(unittest.TestCase):
    def test_sample(self):
        self.assertTrue(is_valid_phone("9587456281"))
        self.assertFalse(is_valid_phone("1252478965"))
        self.assertFalse(is_valid_phone("958745628"))
        self.assertFalse(is_valid_phone("95874562810"))


class TestParsingEmailAddresses(unittest.TestCase):
    def test_sample(self):
        lines = ["DEXTER <dexter@hotmail.com>", "VIRUS <virus!@variable.:p>"]
        self.assertEqual(valid_named_emails(lines), ["DEXTER <dexter@hotmail.com>"])


class TestHexColorCode(unittest.TestCase):
    def test_sample(self):
        css = [
            "#BED", "{", "    color: #FfFdF8; background-color:#aef;", "    font-size: 123px;",
            "    background: -webkit-linear-gradient(top, #f9f9f9, #fff);", "}",
            "#Cab", "{", "    background-color: #ABC;", "    border: 2px dashed #fff;", "}",
        ]
        self.assertEqual(hex_colors(css), ["#FfFdF8", "#aef", "#f9f9f9", "#fff", "#ABC", "#fff"])

    def test_rejects_wrong_length(self):
        self.assertEqual(hex_colors(["color: #abcd;"]), [])


class TestHtmlParserPart1(unittest.TestCase):
    def test_sample(self):
        html = '<html><head><title>HTML Parser - I</title></head>' \
               '<body data-modal-target class=\'1\'><h1>HackerRank</h1><br /></body></html>'
        self.assertEqual(html_parser_part_1.parse(html), [
            "Start : html", "Start : head", "Start : title", "End   : title", "End   : head",
            "Start : body", "-> data-modal-target > None", "-> class > 1", "Start : h1",
            "End   : h1", "Empty : br", "End   : body", "End   : html",
        ])


class TestHtmlParserPart2(unittest.TestCase):
    def test_sample(self):
        html = "<!--[if IE 9]>IE9-specific content\n<![endif]-->\n<div> Welcome to HackerRank</div>\n<!--[if IE 9]>IE9-specific content<![endif]-->"
        self.assertEqual(html_parser_part_2.parse(html), [
            ">>> Multi-line Comment", "[if IE 9]>IE9-specific content\n<![endif]",
            ">>> Data", " Welcome to HackerRank",
            ">>> Single-line Comment", "[if IE 9]>IE9-specific content<![endif]",
        ])


class TestHtmlTagsAttributes(unittest.TestCase):
    def test_sample(self):
        html = '<head>\n<title>HTML</title>\n</head>\n<object type="application/x-flash"\n' \
               '  data="your-file.swf"\n  width="0" height="0">\n  <!-- <param name="movie" value="your-file.swf" /> -->\n' \
               '  <param name="quality" value="high"/>\n</object>'
        self.assertEqual(html_tags_attributes.parse(html), [
            "head", "title", "object", "-> type > application/x-flash", "-> data > your-file.swf",
            "-> width > 0", "-> height > 0", "param", "-> name > quality", "-> value > high",
        ])


class TestUid(unittest.TestCase):
    def test_sample(self):
        self.assertFalse(is_valid_uid("B1CD102354"))
        self.assertTrue(is_valid_uid("B1CDEF2354"))

    def test_rejects_symbols(self):
        self.assertFalse(is_valid_uid("AB#1234567"))


class TestCreditCardNumbers(unittest.TestCase):
    def test_valid(self):
        for s in ("4123456789123456", "5123-4567-8912-3456", "4123356789123456"):
            self.assertTrue(is_valid_card(s), s)

    def test_invalid(self):
        for s in ("61234-567-8912-3456", "5133-3367-8912-3456", "5123 - 3567 - 8912 - 3456",
                  "44244x4424442444", "0525362587961578"):
            self.assertFalse(is_valid_card(s), s)


class TestPostalCodes(unittest.TestCase):
    def test_sample(self):
        self.assertFalse(is_valid_postal_code("110000"))
        self.assertTrue(is_valid_postal_code("523563"))
        self.assertFalse(is_valid_postal_code("552523"))
        self.assertFalse(is_valid_postal_code("012345"))


class TestMatrixScript(unittest.TestCase):
    def test_sample(self):
        rows = ["Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "ir!"]
        self.assertEqual(decode(rows), "This is Matrix#  %!")


if __name__ == "__main__":
    unittest.main()
