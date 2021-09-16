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

Doctests for fizzbuzz function:
#to run them use 'pytest --doctest-modules' command

# Positive tests
# Testing that function works correctly with positive n
>>> list(fizzbuzz(5))
['1', '2', 'fizz', '4', 'buzz']

# Testing that function works correctly with n = 15
>>> list(fizzbuzz(15))[-1]
'fizz buzz'

# Testing that function will give an empty list as the result with n = 0
>>> list(fizzbuzz(0))
[]

# Testing that function will give an empty list as the result with n < 0
>>> list(fizzbuzz(-5))
[]

# Negative test
# Testing that function will raise TypeError if n is not int
>>> list(fizzbuzz('fifteen'))
Traceback (most recent call last):
    ...
TypeError: ...

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
