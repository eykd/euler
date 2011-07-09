# -*- coding: utf-8 -*-
"""util -- utility functions for the Euler Project.
"""
import operator
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
    _chunk_size = 1000
    _found_sorted = deque([2,3,5])
    _found = set(_found_sorted)
    _candidates = set()
    _candidates_sorted = []
    _chunk_max = 1
    _n = 7

    @property
    def chunk_size(self):
        return PrimeFactory._chunk_size

    @chunk_size.setter
    def chunk_size(self, val):
        PrimeFactory._chunk_size = val

    @property
    def _primes_gen(self):
        #print "Creating primes generator..."
        PrimeFactory._primes_gen = PrimeFactory._generate_primes()
        #print "Priming the pump."
        PrimeFactory._primes_gen.next()
        return PrimeFactory._primes_gen

    def primes(self, max_term=None, max_step=None):
        i = 0
        while True:
            try:
                n = self._found_sorted[i]
            except IndexError:
                previously = len(self._found_sorted)
                while len(self._found_sorted) == previously:
                    #print "Ran out of primes. Generating more..."
                    self._primes_gen.next()  # <-- this won't always extend self._found_sorted.
                n = self._found_sorted[i]

            if max_term is None or n <= max_term:
                #print n
                yield n
            else:
                break

            i += 1

            if max_step is not None and i == max_step:
                break

    def __iter__(self):
        return self.primes()

    def __call__(self, max_term=None, max_step=None):
        return 

    @classmethod
    def _generate_primes(klass):
        return klass.sieve_of_eratosthenes()

    @staticmethod
    def sieve_1(n, candidates, max_term, max_sqrt=None):
        #print "Sieving %s candidates by %s" % (len(candidates), n)
        #print "Candidates:", candidates
        if not candidates:
            return
        min_c = min(candidates)
        #t = n * ((min_c / n) + 1)  ### SLOW...
        t = n * 2
        #print "Starting w/", t
        while t < max_term:
            if t >= min_c and t in candidates:
                candidates.remove(t)
            t += n
        #print "Candidates remaining:", candidates

    @staticmethod
    def sieve_2(n, candidates, max_term, max_sqrt):
        #print "Sieving %s candidates by %s" % (len(candidates), n)
        #print "Candidates:", candidates
        if not candidates:
            return
        min_c = min(candidates)
        
        #print "Starting w/", n*3
        for t in xrange(3*n, max_term, n*2):
            if t >= min_c and t in candidates and t <= max_sqrt:
                candidates.remove(t)
        #print "Candidates remaining:", candidates
                

    @classmethod
    def sieve_of_eratosthenes(klass):
        """http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
        """
        sieve = klass.sieve_1
        sieve = klass.sieve_2
        
        while True:
            if klass._n >= klass._chunk_max:
                # Reset the candidates with the next range.
                klass._chunk_max += klass._chunk_size
                klass._chunk_max_sqrt = int(klass._chunk_max**0.5)
                klass._candidates_sorted[:] = sorted(klass._candidates)
                #print "Found %s primes." % (len(klass._candidates_sorted))
                #print "Sorting them..."
                klass._found.update(klass._candidates)
                klass._found_sorted.extend(klass._candidates_sorted)
                klass._candidates.clear()
                yield None
                klass._candidates.update(xrange(klass._n, klass._chunk_max, 2))
                #print "Generating next chunk of %s... (%s to %s)" % (klass._chunk_size, klass._n, klass._chunk_max-1)
                for x in klass._found_sorted:
                    sieve(x, klass._candidates, klass._chunk_max, klass._chunk_max_sqrt)
            if klass._n in klass._candidates:
                sieve(klass._n, klass._candidates, klass._chunk_max, klass._chunk_max_sqrt)
            klass._n += 1

primes = PrimeFactory()


def fast_primes(n):
    """Input n>=6, Returns a list of primes, 2 <= p < n

    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """
    correction = int(n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
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


def product(n):
    return reduce(operator.mul, n)
