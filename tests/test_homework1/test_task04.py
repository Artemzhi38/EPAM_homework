from homeworks.homework1.task04 import check_sum_of_four


def test_n_is_2_case():
    """Testing that function gives right result with N = 2"""
    a = [0, 1]
    b = [0, 1]
    c = [0, -1]
    d = [0, -1]
    assert check_sum_of_four(a, b, c, d) == 6


def test_only_positive_case():
    """Testing that function gives right result
        with only positive elements in lists"""
    a = [1, 1, 1, 1, 1]
    b = [1, 1, 1, 1, 1]
    c = [1, 1, 1, 1, 1]
    d = [1, 1, 1, 1, 1]
    assert check_sum_of_four(a, b, c, d) == 0


def test_empty_lists_case():
    """Testing that function gives right result with empty lists"""
    a = []
    b = []
    c = []
    d = []
    assert check_sum_of_four(a, b, c, d) == 0


def test_n_is_10_worst_case():
    """Testing that function takes an appropriate time to work"""
    a = []
    b = []
    c = []
    d = []
    for i in range(10):
        a.append(0)
        b.append(0)
        c.append(0)
        d.append(0)
    assert check_sum_of_four(a, b, c, d) == 10000
