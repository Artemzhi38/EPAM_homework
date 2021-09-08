from homeworks.homework2.task3 import combinations


def test_example():
    """Testing that function gives right result with default example"""
    assert combinations([1, 2], [3, 4]) == [
        [1, 3],
        [1, 4],
        [2, 3],
        [2, 4],
    ]


def test_diff_length_lists_example():
    """Testing that function gives right result with different lengths
     of lists example"""
    assert combinations([1, 2], [3, 4, 5]) == [
        [1, 3],
        [1, 4],
        [1, 5],
        [2, 3],
        [2, 4],
        [2, 5],
    ]
