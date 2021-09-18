import time

from homeworks.homework3.task2 import pool_count, slow_calculate


def test_for_taken_time():
    """Testing that function takes less than
    minute to perform"""
    start = time.time()
    pool_count(501)
    end = time.time()
    assert end-start < 60


def test_for_right_result():
    """Testing that function gives right result"""
    res = 0
    for value in range(5):
        res += slow_calculate(value)
    assert pool_count(5) == res
