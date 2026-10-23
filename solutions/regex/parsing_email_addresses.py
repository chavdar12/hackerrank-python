from email.utils import parseaddr
from re import fullmatch


def valid_named_emails(lines):
    pattern = r"[a-zA-Z][\w\-.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}"
    return [line for line in lines if fullmatch(pattern, parseaddr(line)[1])]
