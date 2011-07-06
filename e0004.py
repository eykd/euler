# -*- coding: utf-8 -*-
"""e00004 -- http://projecteuler.net/index.php?section=problems&id=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import pprint
from collections import deque
import itertools as it

from util import numbersOfLength


def isPalindrome(x):
    return x == int(''.join(reversed(str(x))))


def isPalindrome_test():
    assert isPalindrome(9009)
    assert not isPalindrome(9000)


def main():
    max_pal = None
    for a, b in it.product(numbersOfLength(3), numbersOfLength(3)):
        p = a*b
        if isPalindrome(p) and p > max_pal:
            max_pal = a*b
    return max_pal


if __name__ == '__main__':
    print __doc__
    result = main()
    if result:
        pprint.pprint(result)
else:
    from nose.tools import *
