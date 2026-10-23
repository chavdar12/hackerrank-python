from datetime import datetime

FORMAT = "%a %d %b %Y %H:%M:%S %z"


def time_delta(t1, t2):
    diff = datetime.strptime(t1, FORMAT) - datetime.strptime(t2, FORMAT)
    return str(int(abs(diff.total_seconds())))
