# Here's a not very efficient calculation function that
# calculates something important:

import hashlib
import queue
import random
import struct
import time
from multiprocessing import Pool, Process, Queue


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))

# Calculate total sum of slow_calculate() of all numbers starting from
# 0 to 500. Calculation time should not take more than a minute. Use
# functional capabilities of multiprocessing module. You are not allowed
# to modify slow_calculate function.


def do_count(values_to_count, counted_values):
    while True:
        try:
            value = values_to_count.get_nowait()
        except queue.Empty:
            break
        else:
            counted_values.put(slow_calculate(value))
    return True


def pool_count(n):
    p = Pool(32)
    return sum(p.map(slow_calculate, range(n)))
