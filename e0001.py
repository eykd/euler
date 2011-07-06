# -*- coding: utf-8 -*-
"""e00001 -- http://projecteuler.net/index.php?section=problems&id=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import pprint


def main():
    return sum(x for x in xrange(1, 1000) if not x % 3 or not x % 5)


def main_test():
    assert_equal(main(), 233168)


if __name__ == '__main__':
    pprint.pprint(main())
else:
    from nose.tools import *

