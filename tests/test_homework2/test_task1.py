from homeworks.homework2.task1 import (count_non_ascii_chars,
                                       count_punctuation_chars,
                                       get_longest_diverse_words,
                                       get_most_common_non_ascii_char,
                                       get_rarest_char)


def test_get_longest_diverse_words_func():
    """Testing that function get_longest_diverse_words gives right result"""
    assert get_longest_diverse_words('C:\\Users\\auto\\Desktop\\'
                                     'Programming\\Python\\'
                                     'EPAM_training\\EPAM_homework'
                                     '\\tests\\test_homework2\\test_files\\'
                                     'testfile1_task1.txt') == \
           ['hijklmnoа', 'hijklmno1', 'stuvwxyz1', 'hijklmno2', 'stuvwxyz2',
            'hijklmno3', 'stuvwxyz3', 'defgб', 'hijklmnoб', 'stuvwxyzб']


def test_get_rarest_char_func():
    """Testing that that function get_rarest_char gives right result"""
    assert get_rarest_char('C:\\Users\\auto\\Desktop\\Programming\\Python\\'
                           'EPAM_training\\EPAM_homework\\tests\\'
                           'test_homework2\\test_files\\'
                           'testfile1_task1.txt') == '9'


def test_count_punctuation_chars_func():
    """Testing that that function count_punctuation_chars gives right result"""
    assert count_punctuation_chars('C:\\Users\\auto\\Desktop\\Programming'
                                   '\\Python\\EPAM_training\\'
                                   'EPAM_homework\\tests\\test_homework2'
                                   '\\test_files\\testfile1_task1.txt') == 20


def test_count_non_ascii_chars_func():
    """Testing that that function count_non_ascii_chars gives right result"""
    assert count_non_ascii_chars('C:\\Users\\auto\\Desktop\\Programming'
                                 '\\Python\\EPAM_training\\EPAM_homework'
                                 '\\tests\\test_homework2\\test_files\\'
                                 'testfile1_task1.txt') == 9


def test_get_most_common_non_ascii_char_func():
    """Testing that that function get_most_common_non_ascii_char gives
    right result"""
    assert get_most_common_non_ascii_char('C:\\Users\\auto\\Desktop\\'
                                          'Programming\\Python\\EPAM_training'
                                          '\\EPAM_homework\\tests\\'
                                          'test_homework2\\test_files\\'
                                          'testfile1_task1.txt') == 'б'
