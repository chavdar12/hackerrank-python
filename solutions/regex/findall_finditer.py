import re

CONSONANT = "[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]"


def vowel_runs(s):
    runs = re.findall(r"(?<=%s)([AEIOUaeiou]{2,})(?=%s)" % (CONSONANT, CONSONANT), s)
    return runs or [-1]
