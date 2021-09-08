"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.
Write a function that accept any iterable of unique values and then
it behaves as range function:
import string
assert = custom_range(string.ascii_lowercase, 'g') ==
['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') ==
['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) ==
['p', 'n', 'l', 'j', 'h']
"""
from typing import Any, Iterable, List


def custom_range(*args, **kwargs) -> List[Any]:

    def one_param(coll: Iterable, stop: Any) -> List[Any]:
        """Function to use when only stop argument is stated"""
        result = []
        for element in coll:
            if element != stop:
                result.append(element)
            else:
                return result

    def two_or_three_params(coll: Iterable, start: Any,
                            stop: Any, step=1) -> List[Any]:
        """Function to use when start and step argument are stated"""
        result = []
        collection = list(coll)
        if step < 0:
            collection.reverse()
            step = abs(step)
        index = collection.index(start)
        while index < collection.index(stop):
            result.append(collection[index])
            index += step
        return result

    '''Here we decide which function to chose'''
    if len(args)+len(kwargs) < 3:
        return one_param(*args, **kwargs)
    else:
        return two_or_three_params(*args, **kwargs)
