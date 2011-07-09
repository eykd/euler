# -*- coding: utf-8 -*-
"""e0011 -- http://projecteuler.net/index.php?section=problems&id=11

***Not sure where this came from. It's not #11.

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
import pprint

def sumdigits(n):
    return sum(int(d) for d in str(n))


def sumdigits_test():
    assert_equal(
        sumdigits(2**15),
        26)

def main():
    return sumdigits(2**1000)


if __name__ == '__main__':
    print __doc__
    result = main()
    if result:
        pprint.pprint(result)
else:
    from nose.tools import *
