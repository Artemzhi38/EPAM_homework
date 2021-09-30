from homeworks.homework7.task1 import example_tree, find_occurrences


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
    assert find_occurrences(example_tree, True) == 10


def test_counting_tuple_element():
    """Testing that function finds all tuple elements"""
    example_tree[(2, 1)] = {1, 2, 3, 4, (2, 1)}
    assert find_occurrences(example_tree, (2, 1)) == 2
