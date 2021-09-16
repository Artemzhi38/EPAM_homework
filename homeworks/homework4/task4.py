"""
Write a function that takes a number N as an
input and returns N FizzBuzz numbers*
Write a doctest for that function.

Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - doctests are run with pytest command

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests


* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15,
"Робот Фортран, чисть картошку!"

Doctests for fizzbuzz function:
#to run them use 'pytest --doctest-modules' command

# Positive tests
# Testing that function works correctly with positive n
>>> fizzbuzz(5)
['1', '2', 'fizz', '4', 'buzz']

# Testing that function works correctly with n = 15
>>> fizzbuzz(15)[-1]
'fizz buzz'

# Testing that function will give an empty list as the result with n = 0
>>> fizzbuzz(0)
[]

# Testing that function will give an empty list as the result with n < 0
>>> fizzbuzz(-5)
[]

# Negative test
# Testing that function will raise TypeError if n is not int
>>> fizzbuzz('fifteen')
Traceback (most recent call last):
    ...
TypeError: ...

"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    result = []
    for i in range(1, n+1):
        if int(i) % 15 == 0:
            result.append("fizz buzz")
        elif int(i) % 5 == 0:
            result.append("buzz")
        elif int(i) % 3 == 0:
            result.append("fizz")
        else:
            result.append(str(i))
    return result
