"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List


def find_maximal_sub_array_sum(nums: List[int], k: int) -> int:
    max_sum = nums[0]
    if k < 1:
        raise ValueError
    for i in range(len(nums)-k+1):
        s = nums[i]
        if s > max_sum:
            max_sum = s
        for j in range(1, k):
            if nums[i+j] > max_sum:
                max_sum = nums[i+j]
            s += nums[i+j]
            if s > max_sum:
                max_sum = s
    return max_sum
