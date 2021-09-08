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
    result = ['', '', '', '', '', '', '', '', '', '']
    with open(file_path,
              mode='r', encoding='raw_unicode_escape') as text:
        for line in text:
            for word in re.sub(r'\W', ' ', line).split():
                if word not in result:
                    for element in result:
                        if len(element) < len(word):
                            result.remove(element)
                            result.append(word)
                            break
                        if len(element) == len(word) and \
                                len(set(element)) < len(set(word)):
                            result.remove(element)
                            result.append(word)
                            break
    return result


def get_rarest_char(file_path: str) -> str:
    counter = {}
    with open(file_path,
              mode='r', encoding='raw_unicode_escape') as text:
        first = text.readline()[0]
        for line in text:
            for symbol in line:
                if symbol in counter.keys():
                    counter[symbol] += 1
                else:
                    counter[symbol] = 1
    rarest_count = counter[first]
    rarest = first
    for symbol in counter:
        if counter[symbol] < rarest_count:
            rarest_count = counter[symbol]
            rarest = symbol
    return rarest


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
                        if counter == {}:
                            first = symbol
                        if symbol in counter.keys():
                            counter[symbol] += 1
                        else:
                            counter[symbol] = 1
    most_common_count = counter[first]
    most_common = first
    for symbol in counter:
        if counter[symbol] > most_common_count:
            most_common_count = counter[symbol]
            most_common = symbol
    return most_common
