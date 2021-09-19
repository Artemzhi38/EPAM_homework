"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import re
from typing import List
from unicodedata import category


def get_longest_diverse_words(file_path: str) -> List[str]:
    words = []
    with open(file_path,
              mode='r', encoding='raw_unicode_escape') as text:
        for line in text:
            for word in re.sub(r'\W', ' ', line).split():
                if word not in words:
                    words.append(word)
    result = sorted(words, reverse=True, key=lambda element:
                    (len(set(element)), len(element)))
    return result[:10]


def get_rarest_char(file_path: str) -> str:
    counter = {}
    with open(file_path,
              mode='r', encoding='raw_unicode_escape') as text:
        for line in text:
            for symbol in line:
                if symbol in counter:
                    counter[symbol] += 1
                else:
                    counter[symbol] = 1
    sorted_chars = sorted(counter, key=lambda x: counter[x])
    return sorted_chars[0]


def count_punctuation_chars(file_path: str) -> int:
    counter = 0
    with open(file_path,
              mode='r', encoding='raw_unicode_escape') as text:
        for line in text:
            for symbol in line:
                if category(symbol)[0] in ['p', 'P']:
                    counter += 1
    return counter


def count_non_ascii_chars(file_path: str) -> int:
    counter = 0
    with open(file_path,
              mode='r', encoding='raw_unicode_escape') as text:
        for line in text:
            if not line.isascii():
                for symbol in line:
                    if not symbol.isascii():
                        counter += 1
    return counter


def get_most_common_non_ascii_char(file_path: str) -> str:
    counter = {}
    with open(file_path,
              mode='r', encoding='raw_unicode_escape') as text:
        for line in text:
            if not line.isascii():
                for symbol in line:
                    if not symbol.isascii():
                        if symbol in counter:
                            counter[symbol] += 1
                        else:
                            counter[symbol] = 1
    sorted_chars = sorted(counter, key=lambda x: counter[x],
                          reverse=True)
    return sorted_chars[0]
