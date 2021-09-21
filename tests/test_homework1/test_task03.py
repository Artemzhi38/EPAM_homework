from homeworks.homework1.task03 import find_maximum_and_minimum


def test_positive_case():
    """Testing that function gives right result with positive integers"""
    assert find_maximum_and_minimum('tests/test_homework1/test_files/'
                                    'testfile1_task03.txt') == (1, 5)


def test_negative_case():
    """Testing that function gives right result with positive integers"""
    assert find_maximum_and_minimum('tests/test_homework1/test_files/'
                                    'testfile2_task03.txt') == (-5, 5)
