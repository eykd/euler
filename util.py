# -*- coding: utf-8 -*-
"""util -- utility functions for the Euler Project.
"""
from collections import deque
from nose.tools import *


def factor(n):
    factors = deque()
    for x in primes:
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


def fib(max_term=4000000, max_n=None):
    n = 0
    a = 0
    b = 1
    while b < max_term and (max_n is None or n < max_n):
        c = a + b
        a = b
        b = c
        yield c
        n += 1

def fib_test():
    assert_equal(
        list(fib(max_n=10)),
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
    _chunk_size = 100
    _found = set()
    _found_sorted = deque()
    _candidates = set()
    _candidates_sorted = []
    _chunk_max = 1
    _n = 2
    _primes = None

    def __init__(self):
        if PrimeFactory._primes is None:
            PrimeFactory._primes = self._generate_primes()
            PrimeFactory._primes.next()

    @classmethod
    def primes(klass, max_term=None, max_n=None):
        i = 0
        while True:
            try:
                n = klass._found_sorted[i]
            except IndexError:
                klass._primes.next()
                n = klass._found_sorted[i]

            if max_term is None or n <= max_term:
                yield n
            else:
                break

            i += 1

            if max_n is not None and i == max_n:
                break

    def __iter__(self):
        return self.primes()

    @staticmethod
    def sieve(n, candidates, max_term):
        #print "Sieving %s candidates by %s" % (len(candidates), n)
        if not candidates:
            return
        min_c = min(candidates)
        t = n*2
        while t < max_term:
            if t >= min_c:
                try:
                    candidates.remove(t)
                except KeyError:
                    pass
            t += n
        #print candidates

    @classmethod
    def _generate_primes(klass):
        while True:
            if klass._n >= klass._chunk_max:
                # Reset the candidates with the next range.
                klass._chunk_max += klass._chunk_size
                klass._candidates_sorted[:] = sorted(klass._candidates)
                klass._found.update(klass._candidates)
                klass._found_sorted.extend(klass._candidates_sorted)
                klass._candidates.clear()
                yield None
                klass._candidates.update(xrange(klass._n, klass._chunk_max))
                for x in klass._found_sorted:
                    klass.sieve(x, klass._candidates, klass._chunk_max)
            if klass._n in klass._candidates:
                klass.sieve(klass._n, klass._candidates, klass._chunk_max)
            klass._n += 1

primes = PrimeFactory()


