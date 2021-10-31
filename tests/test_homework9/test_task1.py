import os.path

import pytest

from homeworks.homework9.task1 import merge_sorted_files


@pytest.fixture()
def one_file_fixture():
    path1 = os.path.join(os.path.dirname(__file__), 'file1.txt')
    with open(path1, 'w') as test_file:
        test_file.writelines(["1\n", "2\n", "3\n"])
    return [path1]


@pytest.fixture()
def two_files_fixture():
    path1 = os.path.join(os.path.dirname(__file__), 'file1.txt')
    with open(path1, 'w') as test_file:
        test_file.writelines(["0\n", "4\n", "5\n"])
    path2 = os.path.join(os.path.dirname(__file__), 'file2.txt')
    with open(path2, 'w') as test_file:
        test_file.writelines(["1\n", "2\n", "3\n"])
    return [path1, path2]


@pytest.fixture()
def two_files_one_empty_fixture():
    path1 = os.path.join(os.path.dirname(__file__), 'file1.txt')
    with open(path1, 'w') as test_file:
        test_file.writelines([""])
    path2 = os.path.join(os.path.dirname(__file__), 'file2.txt')
    with open(path2, 'w') as test_file:
        test_file.writelines(["200\n", "400\n", "600\n"])
    return [path1, path2]


@pytest.fixture()
def three_files_fixture():
    path1 = os.path.join(os.path.dirname(__file__), 'file1.txt')
    with open(path1, 'w') as test_file:
        test_file.writelines(["3\n", "4\n"])
    path2 = os.path.join(os.path.dirname(__file__), 'file2.txt')
    with open(path2, 'w') as test_file:
        test_file.writelines(["2\n", "5\n", "8\n"])
    path3 = os.path.join(os.path.dirname(__file__), 'file3.txt')
    with open(path3, 'w') as test_file:
        test_file.writelines(["1\n", "6\n", "7\n", "9\n", "10\n"])
    return [path1, path2, path3]


def test_one_file(one_file_fixture):
    """Testing that function returns right result when
    given a list with one path to file"""
    assert list(merge_sorted_files(one_file_fixture)) == [1, 2, 3]


def test_two_files(two_files_fixture):
    """Testing that function returns right result when
    given a list with two paths to files with same
    lengths"""
    assert list(merge_sorted_files(two_files_fixture)) == [0, 1, 2, 3, 4, 5]


def test_two_files_one_empty(two_files_one_empty_fixture):
    """Testing that function returns right result when
    given a list with two paths to files and one of
    them is empty"""
    assert list(merge_sorted_files(two_files_one_empty_fixture)) == [200,
                                                                     400,
                                                                     600]


def test_three_files(three_files_fixture):
    """Testing that function returns right result when
    given a list with two paths to files with and each
    of them has different length"""
    assert list(merge_sorted_files(three_files_fixture)) == [1, 2, 3, 4, 5,
                                                             6, 7, 8, 9, 10]
