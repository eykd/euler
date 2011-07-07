# -*- coding: utf-8 -*-
"""e0009 -- http://projecteuler.net/index.php?section=problems&id=9

A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math
import pprint
from collections import deque


def main():
    # Map all the squares from 1 to 999.
    num_square = dict()
    square_num = dict()
    for x in xrange(1, 1000):
        sq = x**2
        num_square[x] = sq
        square_num[sq] = x

    # Using our mapping, find combos candidate values for c by
    # checking a^2 + b^2 against our reverse mapping.
    for a in xrange(1, 500):
        asq = num_square[a]
        for b in xrange(1, 500):
            bsq = num_square[b]
            if (asq+bsq) in square_num:
                c = square_num[asq+bsq]
                if a + b + c == 1000:
                    print (a,  b,  c)
                    return a * b * c
    


if __name__ == '__main__':
    print __doc__
    result = main()
    if result:
        pprint.pprint(result)
else:
    from nose.tools import *
