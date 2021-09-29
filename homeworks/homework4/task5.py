"""
This task is optional.

Write a generator that takes a number N as an input
and returns a generator that yields N FizzBuzz numbers*
Don't use any ifs, you can find an approach for the
implementation in this video**.


Definition of done:
 - function is created
 - function is properly formatted
 - function has tests

* https://en.wikipedia.org/wiki/Fizz_buzz
** https://www.youtube.com/watch?v=NSzsYWckGd4
"""
# import itertools
# from typing import List, Generator


def fizzbuzz(n: int):
    result = [str(i) for i in range(1, n+1)]
    for i in range(2, n, 3):
        result[i] = 'fizz'
    for i in range(4, n, 5):
        result[i] = 'buzz'
    for i in range(14, n, 15):
        result[i] = 'fizz buzz'

    for element in result:
        yield element
