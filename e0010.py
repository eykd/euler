# -*- coding: utf-8 -*-
"""e0010 -- http://projecteuler.net/index.php?section=problems&id=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math
import pprint
from collections import deque

from util import primes

def sumprimes(max_term=10):
    return sum(primes.primes(max_term=max_term))


def sumprimes_test():
    assert_equal(
        sumprimes(10),
        17)


def main():
    primes.chunk_size = 10000
    return sumprimes(2000000)


if __name__ == '__main__':
    print __doc__
    result = main()
    if result:
        pprint.pprint(result)
else:
    from nose.tools import *