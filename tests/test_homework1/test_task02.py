from homeworks.homework1.task02 import check_fib


def test_min_positive_case():
    """Testing that minimal length of Fibonacci sequence give True"""
    assert check_fib([0, 1, 1])


def test_positive_case():
    """Testing that default Fibonacci sequence give True"""
    assert check_fib([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
                      233, 377, 610, 987, 1597, 2584, 4181, 6765])


def test_alternative_positive_case():
    """Testing that Fibonacci sequence starting not with "0, 1" give True"""
    assert check_fib([2, 4, 6, 10])


def test_negative_case():
    """Testing that non-Fibonacci sequence give False"""
    assert not check_fib([0, 1, 1, 2, 3, 4, 5, 8])


def test_small_sequence_case():
    """Testing that non-Fibonacci sequence give False"""
    assert not check_fib([0, 1])
