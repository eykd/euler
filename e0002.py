# -*- coding: utf-8 -*-
"""e00002 -- http://projecteuler.net/index.php?section=problems&id=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
import pprint

from util import fib


def main():
    return sum(x for x in fib(max_term=4000000) if not x % 2)


def main_test():
    assert_equal(main(),
                 4613732
                 )


if __name__ == '__main__':
    print __doc__
    pprint.pprint(main())
else:
    from nose.tools import *
