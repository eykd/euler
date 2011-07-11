# -*- coding: utf-8 -*-
"""util -- utility functions for the Euler Project.
"""
import operator
from array import array
from collections import deque
from nose.tools import *

def binary_search(a, test, lo=0, hi=None):
    """Perform a binary search of the values in list a, with test(val) providing the test.

    test(val) should return:

    -1 if the value is prior to this item
    1 if the value is after this item
    0 if the value is this item

    Returns -1 if the value is not found.

    http://stackoverflow.com/questions/212358/binary-search-in-python/212413#212413
    """
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        result = test(midval)
        if result == -1:
            lo = mid+1
        elif result == 1:
            hi = mid
        else:
            return mid
    return -1


def factor(n):
    """Return the prime factors of n.
    """
    factors = deque()
    for x in primes():
        while not n % x:
            factors.append(x)
            n = n / x
        if n == 1:
            return factors


def factor_test():
    """The prime factors of 13195 are 5, 7, 13 and 29.
    """
    assert_equal(
        list(factor(13195)),
        [5, 7, 13, 29]
        )


def fib(max_term=4000000, max_step=None):
    n = 0
    a = 0
    b = 1
    while b < max_term and (max_step is None or n < max_step):
        c = a + b
        a = b
        b = c
        yield c
        n += 1

def fib_test():
    assert_equal(
        list(fib(max_step=10)),
        [1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
        )
        

def naturals_to(n):
    return xrange(1, n+1)


def numbersOfLength(n):
    start = int('1' + '0'*(n-1))
    end = int('1' + '0'*(n))
    return xrange(start, end)


def numbersOfLength_test():
    assert_equal(
        list(numbersOfLength(1)),
        range(1, 10)
        )

    assert_equal(
        list(numbersOfLength(2)),
        range(10, 100)
        )


class PrimeFactory(object):
    known_primes = deque([2])

    def __iter__(self):
        return self()

    def __call__(self, max_term=None, max_step=None):
        i = 0
        p = 2
        for p in self.known_primes:
            if max_term is not None and p > max_term:
                return
            elif max_step is not None and i >= max_step:
                return
            else:
                yield p
                i += 1

        last_prime = p

        if max_step is not None:
            max_step -= i

        for p in self.primes(start_prime=last_prime, max_term=max_term, max_step=max_step):
            yield p
    
    def primes(self, max_term=None, max_step=None, start_prime=2):
        """Generate all of the primes."""
        # so first we must consider what makes a prime number.
        # a prime is a number with only two factors - 1 and itself.
        # all integers are either prime or composite - which is to say,
        # all numbers that are not prime have prime factors.
        # got it so far?
        # good.
        # now the next thing - which is also obvious - is that any prime
        # that a number can be divisible by is going to be less than that
        # number.  But this makes our lives a little simpler.
        # shall I proceed to build a simple implementation?  I will
        # intentionally leave out the optimizations at first.
        known_primes = self.known_primes
        if start_prime == 2:
            yield 2 # ignore 2, it’s the only even prime
            x = 3
        else:
            assert start_prime % 2, "Starting prime must be odd or 2."
            x = start_prime + 2
        step = 1
            
        while (max_term is None or x <= max_term) and (max_step is None or step <= max_step):
            prime = True
            for y in known_primes:
                if y ** 2 > x: # stop checking
                    break
                elif x % y == 0: # a factor!
                    prime = False
                    break
            if prime:
                yield x
                try:
                    if x > known_primes[-1]:
                        known_primes.append(x)
                except IndexError:
                    known_primes.append(x)
                step += 1
            x += 2
    
    def fast_primes(self, n):
        """Input n>=6, Returns a list of primes, 2 <= p < n
    
        http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
        """
        correction = int(n%6>1)
        n = {0:n, 1:n-1, 2:n+4, 3:n+3, 4:n+2, 5:n+1}[n%6]
        sieve = [True] * (n/3)
        sieve[0] = False
        for i in xrange(int(n**0.5)/3+1):
            if sieve[i]:
                k = 3*i+1|1
                k_2 = k*k
                k2 = k*2
                sieve[      ((k_2)/3)      ::k2] = [False]*((n/6-(k_2)/6-1)/k+1)
                sieve[(k_2+4*k-2*k*(i&1))/3::k2] = [False]*((n/6-(k_2+4*k-k2*(i&1))/6-1)/k+1)
        return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

primes = PrimeFactory()
    

def product(n):
    return reduce(operator.mul, n)
