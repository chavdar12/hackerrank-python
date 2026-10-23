def validate(s):
    checks = (str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper)
    return tuple(any(check(c) for c in s) for check in checks)
