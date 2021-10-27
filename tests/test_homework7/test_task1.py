import pytest

from homeworks.homework7.task1 import example_tree, find_occurrences


# Positive tests
def test_default_example():
    """Testing that function finds all occurrences
    of element in default example"""
    assert find_occurrences(example_tree, "RED") == 6


def test_expanded_default_example():
    """Testing that function finds all key-occurrences
    and value-occurrences of element"""
    example_tree[True] = True
    example_tree[(True, True)] = {1, 2, 3, 4}
    example_tree["third"][True] = True
    example_tree["third"]["complex_key"][True] = True
    example_tree["third"]["complex_key"]["key3"][4][True] = True
    example_tree["fifth"] = {2: 2, 3: 3, True: True}
    example_tree["sixth"] = [1, 2, 3, [True, 2, 3]]
    assert find_occurrences(example_tree, True) == 13


def test_counting_tuple_element():
    """Testing that function finds all tuple elements"""
    example_tree[(2, 1)] = {1, 2, 3, 4, (2, 1)}
    assert find_occurrences(example_tree, (2, 1)) == 2


# Negative tests
def test_no_such_element():
    """Testing that function returns 0 if there are no
    occurrences of element in tree"""
    assert find_occurrences(example_tree, "red") == 0


def test_tree_is_empty_dict():
    """Testing that function returns 0 if tree is empty"""
    assert find_occurrences({}, "red") == 0


def test_tree_is_not_a_dict():
    """Testing that function raises AttributeError if given not a dict as a tree"""
    with pytest.raises(AttributeError):
        find_occurrences({'red', 'red', 'red'}, "red")

