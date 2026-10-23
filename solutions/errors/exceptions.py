def safe_divide(a, b):
    try:
        return str(int(a) // int(b))
    except (ZeroDivisionError, ValueError) as e:
        return "Error Code: {}".format(e)
