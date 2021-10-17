import os.path

import pytest
from homeworks.homework9.task3 import universal_file_counter


@pytest.fixture()
def one_file_fixture():
    path = os.path.dirname(__file__)
    with open(os.path.join(path, 'file1.txt'), 'w') as f:
        f.writelines([""])
    with open(os.path.join(path, 'file2.txt'), 'w') as f:
        f.writelines([""])
    with open(os.path.join(path, 'file3.txt'), 'w') as f:
        f.writelines(["1 1\n", "2 2\n", "3 3\n", "4 4\n", "5 5\n"])
    return path


@pytest.fixture()
def two_files_fixture():
    path = os.path.dirname(__file__)
    with open(os.path.join(path, 'file1.txt'), 'w') as f:
        f.writelines([""])
    with open(os.path.join(path, 'file2.txt'), 'w') as f:
        f.writelines(["1\n", "2\n", "3\n"])
    with open(os.path.join(path, 'file3.txt'), 'w') as f:
        f.writelines(["1\n", "2\n", "3\n", "4\n", "5\n"])
    return path


@pytest.fixture()
def three_files_fixture():
    path = os.path.dirname(__file__)
    with open(os.path.join(path, 'file1.txt'), 'w') as f:
        f.writelines(["abc\n", "def\n"])
    with open(os.path.join(path, 'file2.txt'), 'w') as f:
        f.writelines(["ghi\n", "jkl\n"])
    with open(os.path.join(path, 'file3.txt'), 'w') as f:
        f.writelines(["mno\n", "pqr\n"])
    return path


@pytest.fixture()
def another_extension_fixture():
    path = os.path.dirname(__file__)
    with open(os.path.join(path, 'file1.doc'), 'w') as f:
        f.write("3 3")
    with open(os.path.join(path, 'file2.doc'), 'w') as f:
        f.write("2 2")
    with open(os.path.join(path, 'file3.doc'), 'w') as f:
        f.write("1 1")
    return path


def test_one_file(one_file_fixture):
    """Testing that function returns right result with
    and without str.split tokenizer when given a dir
    with one non-empty .txt file"""
    assert universal_file_counter(one_file_fixture, "txt") == 5
    assert universal_file_counter(one_file_fixture, "txt", str.split) == 10


def test_two_files(two_files_fixture):
    """Testing that function returns right result with
    and without str.split tokenizer when given a dir
    with two non-empty .txt files"""
    assert universal_file_counter(two_files_fixture, "txt") == 8
    assert universal_file_counter(two_files_fixture, "txt", str.split) == 8


def test_three_files(three_files_fixture):
    """Testing that function returns right result with
    and without list tokenizer when given a dir
    with three non-empty .txt files"""
    assert universal_file_counter(three_files_fixture, "txt") == 6
    assert universal_file_counter(three_files_fixture, "txt", list) == 24


def test_another_extension(another_extension_fixture):
    """Testing that function returns right result with
    and without str.split tokenizer when given a dir
    with three non-empty files with .t extension"""
    assert universal_file_counter(another_extension_fixture, "doc") == 3
    assert universal_file_counter(another_extension_fixture,
                                  "doc", str.split) == 6
