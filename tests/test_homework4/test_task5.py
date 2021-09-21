import types

import pytest

from homeworks.homework4.task5 import fizzbuzz


# Positive tests
def test_function_returns_generator():
    """Testing that function returns generator-class object"""
    assert isinstance(fizzbuzz(1), types.GeneratorType)


def test_function_works_with_positive_n():
    """Testing that function works correctly with n=15"""
    assert list(fizzbuzz(15)) == ['1', '2', 'fizz', '4', 'buzz',
                                  'fizz', '7', '8', 'fizz',
                                  'buzz', '11', 'fizz', '13',
                                  '14', 'fizz buzz']


def test_function_works_with_zero():
    """Testing that function will not yield anything with n = 0"""
    assert list(fizzbuzz(0)) == []


def test_function_works_with_negative_n():
    """Testing that function will not yield anything with n < 0"""
    assert list(fizzbuzz(-5)) == []


# Negative test
def test_function_raise_error_with_non_int_n():
    """Testing that function will raise TypeError if n is not integer"""
    with pytest.raises(TypeError):
        list(fizzbuzz('fifteen'))
