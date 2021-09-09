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


def custom_range(coll: Iterable, start: Any,
                 stop=None, step=1) -> List[Any]:
    result = []
    collection = list(coll)
# checking if amount of input arguments was > 2
# changing start and stop params otherwise
    if stop is None:
        start, stop = collection[0], start
# checking if step argument is negative
# reversing our collection if it is
    if step < 0:
        collection.reverse()
        step = abs(step)
# filling result list
    index = collection.index(start)
    while index < collection.index(stop):
        result.append(collection[index])
        index += step
    return result
