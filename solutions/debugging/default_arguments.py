class OddStream(object):
    current = -1

    def get_next(self):
        self.current += 2
        return self.current


class EvenStream(OddStream):
    current = -2


def values_from_stream(n, stream=None):
    if stream is None:
        stream = EvenStream()
    return [stream.get_next() for _ in range(n)]
