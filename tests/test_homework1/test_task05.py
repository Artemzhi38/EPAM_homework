from homeworks.homework1.task05 import find_maximal_sub_array_sum


def test_default_case():
    """Testing that function gives right result default values"""
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    assert find_maximal_sub_array_sum(nums, k) == 16


def test_1_item_case():
    """Testing that function gives right result with only 1 item in sum"""
    nums = [1, -1, -1, 3, -5, -3, 5, -7]
    k = 3
    assert find_maximal_sub_array_sum(nums, k) == 5


def test_1_item_list_case():
    """Testing that function gives right result with only 1 item in sum"""
    nums = [1]
    k = 1
    assert find_maximal_sub_array_sum(nums, k) == 1
