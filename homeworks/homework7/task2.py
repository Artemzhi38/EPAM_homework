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


def backspace_compare(first: str, second: str):
    for i in re.findall(r"#+", first):
        first = re.sub('[^#]{,'+'{0}'.format(len(i))+'}'+i, "", first)
    for i in re.findall(r"#+", second):
        second = re.sub('[^#]{,'+'{0}'.format(len(i))+'}'+i, "", second)
    return first == second
