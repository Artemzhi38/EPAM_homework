import urllib.request

import pytest
from homeworks.homework4.task2 import count_dots_on_i


# Positive tests
def test_function_works_with_fixture_test_file(monkeypatch):
    """Testing that function given a right url
    counts all 'i' chars in object returned by
    url request"""
    monkeypatch.setattr(urllib.request, 'urlopen',
                        lambda url: ['i' for i in range(10)])
    assert count_dots_on_i('right_url') == 10


# Negative tests
def test_wrong_url():
    """Testing that function given a wrong url
    raises ValueError("Unreachable {url})"""
    url = 'unreachable_url'
    with pytest.raises(ValueError, match=f'Unreachable {url}'):
        count_dots_on_i(url)
