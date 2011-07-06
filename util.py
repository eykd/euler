# -*- coding: utf-8 -*-
"""util -- utility functions for the Euler Project.
"""
from nose.tools import *


def fib(max_term=4000000, max_n=None):
    n = 0
    a = 0
    b = 1
    while b < max_term and (max_n is None or n < max_n):
        c = a + b
        a = b
        b = c
        yield c
        n += 1

def fib_test():
    assert_equal(
        list(fib(max_n=10)),
        [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
        )
        

def numbersOfLength(n):
    start = int('1' + '0'*(n-1))
    end = int('1' + '0'*(n))
    return xrange(start, end)


def numbersOfLength_test():
    assert_equal(
        list(numbersOfLength(1)),
        range(1, 10)
        )

    assert_equal(
        list(numbersOfLength(2)),
        range(10, 100)
        )


