import re


def fun(s):
    return re.match(r"^[a-zA-Z\d_\-]+@[a-zA-Z\d]+\.[a-zA-Z]{1,3}$", s) is not None


def filter_mail(emails):
    return list(filter(fun, emails))
