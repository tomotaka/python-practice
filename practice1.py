#!/usr/bin/python
import pprint
from collections import deque


collatz_len_memo = {}


def collatz(n):
    if n % 2 == 1:
        return n * 3 + 1
    else:
        return n / 2


def collatz_len(n):
    if n in collatz_len_memo:
        return collatz_len_memo[n]
    cl = deque([])
    original = n
    while n != 1:
        if n in collatz_len_memo:
            cl_for_n = collatz_len_memo[n]
            result = len(cl) + cl_for_n
            current_diff = 1
            while 0 < len(cl):
                last = cl.pop()
                collatz_len_memo[last] = cl_for_n + current_diff
                current_diff += 1
            return result
        else:
            cl.append(n)
        n = collatz(n)
    cl.append(1)

    collatz_len_memo[original] = len(cl)
    return len(cl)


def find_max(to):
    max_n = 1
    max_cl = collatz_len(1)
    for i in range(1, to):
        cl = collatz_len(i)
        if max_cl < cl:
            max_n = i
            max_cl = cl

    return [max_n, max_cl]
        

pprint.pprint(find_max(1000000))
