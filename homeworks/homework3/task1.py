"""In previous homework task 4, you wrote a cache function that
remembers other function output value. Modify it to be a
parametrized decorator, so that the following code:

@cache(times=3)
def some_function():
    pass

Would give out cached value up to times number only. Example:

@cache(times=2)
def f():
    return input('? ')
careful with input() in python2, use raw_input() instead

>>> f()
? 1
'1'
>>> f()     # will remember previous value
'1'
>>> f()     # but use it up to two times only
'1'
>>> f()
? 2
'2'
"""
from typing import Callable


def cache(times):
    def inner_cache(func: Callable) -> Callable:
        cache_dict = {}

        def return_func(*args, **kwargs):
            if (*args, *kwargs) in cache_dict.keys():
                if cache_dict[(*args, *kwargs)][0] > 0:
                    cache_dict[(*args, *kwargs)][0] -= 1
                    return cache_dict[(*args, *kwargs)][1]
            cache_dict[(*args, *kwargs)] = [times, func(*args, **kwargs)]
            return cache_dict[(*args, *kwargs)][1]

        return return_func
    return inner_cache


@cache(times=2)
def f():
    return input('? ')
