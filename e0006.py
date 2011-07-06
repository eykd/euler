# -*- coding: utf-8 -*-
"""e0006 -- http://projecteuler.net/index.php?section=problems&id=6

The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
import pprint
from collections import deque, defaultdict

from util import naturals_to


def sumOfSquares(*ns):
    return sum(x**2 for x in ns)


def sumOfSquares_test():
    assert_equal(
        sumOfSquares(*naturals_to(10)),
        385)


def squareOfSum(*ns):
    return sum(ns)**2


def squareOfSum_test():
    assert_equal(
        squareOfSum(*naturals_to(10)),
        3025)


def difference(the_range):
    the_range = list(the_range)
    return squareOfSum(*the_range) - sumOfSquares(*the_range)


def difference_test():
    assert_equal(
        difference(naturals_to(10)),
        2640)


def main():
    return difference(naturals_to(100))
    

if __name__ == '__main__':
    print __doc__
    result = main()
    if result:
        pprint.pprint(result)
else:
    from nose.tools import *
