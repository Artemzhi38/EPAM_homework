import os

import pytest
from homeworks.homework4.task1 import read_magic_number


# Fixture for creating and removing temporary test file
@pytest.fixture()
def path_to_test_file():
    path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        'test.txt')
    yield path
    os.remove(path)


# Positive tests
def test_first_line_of_file_is_integer_1_in_the_interval(
        path_to_test_file):
    """Testing that when first line of the file is
    '1', function gives True"""
    with open(path_to_test_file, "w") as testfile:
        testfile.write("1")
    assert read_magic_number(path_to_test_file)


def test_first_line_of_file_is_integer_3_not_in_the_interval(
        path_to_test_file):
    """Testing that when first line of the file is
    '3', function gives False"""
    with open(path_to_test_file, "w") as testfile:
        testfile.write("3")
    assert not read_magic_number(path_to_test_file)


def test_first_line_of_file_is_float_inside_the_interval(
        path_to_test_file):
    """Testing that when first line of the file is
    '2.0', function gives True"""
    with open(path_to_test_file, "w") as testfile:
        testfile.write("2.0")
    assert read_magic_number(path_to_test_file)


# Negative tests
def test_first_line_of_file_is_not_a_number(
        path_to_test_file):
    """Testing that when first line of the file is
    string, that cannot be converted to number,
    function raises ValueError"""
    with open(path_to_test_file, "w") as testfile:
        testfile.write("one")
    with pytest.raises(ValueError) as err:
        read_magic_number(path_to_test_file)
    assert err.type is ValueError


def test_file_is_empty(path_to_test_file):
    """Testing that when file is empty function raises
     ValueError"""
    with open(path_to_test_file, "w"):
        pass
    with pytest.raises(ValueError) as err:
        read_magic_number(path_to_test_file)
    assert err.type is ValueError


def test_there_is_no_such_file():
    """Testing that when file path is wrong
    function raises ValueError"""
    with pytest.raises(ValueError) as err:
        read_magic_number('clearly_not_a_path_to_test_file')
    assert err.type is ValueError
