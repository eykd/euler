# -*- coding: utf-8 -*-
"""e0007 -- http://projecteuler.net/index.php?section=problems&id=7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
import pprint
from collections import deque, defaultdict

from util import primes


def primes_test():
    p = 0
    for prime in primes.primes(max_step=6):
        p = prime

    assert_equal(p, 13)

def main():
    p = 0
    for prime in primes.primes(max_step=10001):
        p = prime
    return p
    

if __name__ == '__main__':
    print __doc__
    result = main()
    if result:
        pprint.pprint(result)
else:
    from nose.tools import *
