"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
>>> with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


class SupressorCls:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_type == self.exception:
            return True


@contextmanager
def supressor_gen(exception):
    try:
        yield
    except exception:
        pass
