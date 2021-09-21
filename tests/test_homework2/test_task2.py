from homeworks.homework2.task2 import major_and_minor_elem


def test_example1():
    """Testing that function gives right result with first example"""
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)


def test_example2():
    """Testing that function gives right result with second example"""
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test_1_element_in_list():
    """Testing that function gives right result with 1-element-in-list input"""
    assert major_and_minor_elem([1]) == (1, 1)
