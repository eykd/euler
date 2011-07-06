# -*- coding: utf-8 -*-
"""e00003 -- http://projecteuler.net/index.php?section=problems&id=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import pprint
from collections import deque
from util import factor


def main():
    return max(factor(600851475143))


def main_test():
    assert_equal(
        main(),
        6857)


if __name__ == '__main__':
    print __doc__
    result = main()
    if result:
        pprint.pprint(result)
else:
    from nose.tools import *
