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


def multi_proc_count():
    values = 501
    number_of_processes = 64
    values_to_count = Queue()
    counted_values = Queue()
    proc_list = []
    result = 0

    for i in range(values):
        values_to_count.put(str(i))

    for i in range(number_of_processes):
        proc = Process(target=do_count, args=(values_to_count,
                                              counted_values))
        proc_list.append(proc)
        proc.start()

    for proc in proc_list:
        proc.join()

    while not counted_values.empty():
        result += counted_values.get()

    return result


def pool_count(n):
    p = Pool(32)
    return sum(p.map(slow_calculate, range(n)))
