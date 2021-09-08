import string

from homeworks.homework2.task5 import custom_range


def test_default_example_with_only_stop_argument():
    """Testing that function gives right result with default example
     with only stop argument"""
    assert custom_range(string.ascii_lowercase, 'g') == \
           ['a', 'b', 'c', 'd', 'e', 'f']


def test_default_example_with_start_and_stop_arguments():
    """Testing that function gives right result with default example
    with start and stop arguments."""
    assert custom_range(string.ascii_lowercase, 'g', 'p') == \
           ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']


def test_default_example_with_start_stop_and_step_arguments():
    """Testing that function gives right result with default example
    with start, stop and step arguments. Step argument is negative."""
    assert custom_range(string.ascii_lowercase, 'p', 'g', -2) == \
           ['p', 'n', 'l', 'j', 'h']
