"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that
    A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List


def check_sum_of_four(a: List[int], b: List[int],
                      c: List[int], d: List[int]) -> int:
    count = 0
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    for i in range(len(a)):
        if (b[0]+c[0]+d[0]) <= -(a[i]) <= (b[-1]+c[-1]+d[-1]):
            for j in range(len(b)):
                if (c[0]+d[0]) <= -(a[i]+b[j]) <= (c[-1]+d[-1]):
                    for k in range(len(c)):
                        if (d[0]) <= -(a[i]+b[j]+c[k]) <= (d[-1]):
                            for m in range(len(d)):
                                if a[i]+b[j]+c[k]+d[m] == 0:
                                    count += 1
                                elif a[i]+b[j]+c[k]+d[m] > 0:
                                    break
    return count
