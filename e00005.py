# -*- coding: utf-8 -*-
"""e00005 -- http://projecteuler.net/index.php?section=problems&id=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import pprint
from collections import deque, defaultdict

from util import primes, factor


def smallestDivisibleByRange(start, end):
    factor_count = defaultdict(lambda: 1)

    # Analyze the maximum number of times a factor appears.
    for n in xrange(max(start, 2), end+1):
        local_count = defaultdict(lambda: 0)
        factors = factor(n)
        for f in factors:
            local_count[f] += 1

        for f, count in local_count.iteritems():
            factor_count[f] = max(factor_count[f], count)


    n = 1
    for f, count in factor_count.iteritems():
        n *= (f**count)
            
    for d in range(max(start, 2), end+1):
        assert not n % d, (n, d)

    return n

def smallestDivisibleByRange_test():
    assert_equal(
        smallestDivisibleByRange(1, 10),
        2520)

    assert_equal(
        smallestDivisibleByRange(1, 20),
        232792560
        )

def main():
    return smallestDivisibleByRange(1, 20)
    

if __name__ == '__main__':
    print __doc__
    result = main()
    if result:
        pprint.pprint(result)
else:
    from nose.tools import *
