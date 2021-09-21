import urllib.request

import pytest

from homeworks.homework4.task2 import count_dots_on_i


# Positive tests
def test_function_works_with_fixture_test_file(monkeypatch):
    """Testing that function given a right url
    counts all 'i' chars in object returned by
    url request, where is 10 'i' chars"""
    monkeypatch.setattr(urllib.request, 'urlopen',
                        lambda url: ['i' for i in range(10)])
    assert count_dots_on_i('right_url') == 10


def test_function_works_with_empty_file(monkeypatch):
    """Testing that function given a right url
    gives 0 if object returned by
    url request has no 'i' chars in it"""
    monkeypatch.setattr(urllib.request, 'urlopen',
                        lambda url: [])
    assert count_dots_on_i('right_url') == 0


def test_function_works_with_file_consisting_not_only_of_i_chars(monkeypatch):
    """Testing that function given a right url
    gives right result if object returned by
    url request has other chars except 'i' in it"""
    monkeypatch.setattr(urllib.request, 'urlopen',
                        lambda url: [['ijk' for i in range(10)]
                                     for j in range(10)])
    assert count_dots_on_i('right_url') == 100


# Negative tests
def test_wrong_url():
    """Testing that function given a wrong url
    raises ValueError("Unreachable {url})"""
    url = 'unreachable_url'
    with pytest.raises(ValueError, match=f'Unreachable {url}'):
        count_dots_on_i(url)
