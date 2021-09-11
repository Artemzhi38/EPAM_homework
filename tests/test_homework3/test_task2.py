import hashlib
import struct
import time

from homeworks.homework3.task2 import multi_proc_count


def test_for_taken_time():
    """Testing that function takes less than
    minute to perform"""
    start = time.time()
    multi_proc_count()
    end = time.time()
    assert end-start < 60


def test_for_right_result():
    """Testing that function gives right result"""
    res = 0
    for value in range(501):
        data = hashlib.md5(str(value).encode()).digest()
        res += sum(struct.unpack('<' + 'B' * len(data), data))
    assert multi_proc_count() == res
