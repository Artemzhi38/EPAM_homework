"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def return_func(*args, **kwargs):
        if (*args, *kwargs) in cache_dict.keys():
            return cache_dict[(*args, *kwargs)]
        cache_dict[(*args, *kwargs)] = func(*args, **kwargs)
        return cache_dict[(*args, *kwargs)]

    return return_func
