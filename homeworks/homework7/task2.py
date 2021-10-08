"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.
Note that after backspacing an empty text, the text will continue empty.
Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".
    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".
    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".
"""
import re

from collections import defaultdict


def backspace_compare(first: str, second: str):
    result = defaultdict(list)

    for string in first, second:
        for char in string:
            result[string].append(char) if char != '#' \
                else result[string].pop() if len(result[string]) > 0 else 0

    return result[first] == result[second]


'''def backspace_compare_regex(first: str, second: str):
    return re.sub('#', '\b', first) == re.sub('#', '\b', second)'''
