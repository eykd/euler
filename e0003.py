# -*- coding: utf-8 -*-
"""e00003 -- http://projecteuler.net/index.php?section=problems&id=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import pprint
from collections import deque


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
    def primes(klass, max_term=None):
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
                raise StopIteration()

            i += 1

    def __iter__(self):
        return self.primes()

    @staticmethod
    def sieve(n, candidates, max_term):
        #print "Sieving %s candidates by %s" % (len(candidates), n)
        if not candidates:
            return
        min_c = min(candidates)
        max_c = max(candidates)
        t = n*2
        while t < max_term and t <= max_c:
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


def factor(n):
    factors = deque()
    for x in primes:
        while not n % x:
            factors.append(x)
            n = n / x
        if n == 1:
            return factors


def main():
    return max(factor(600851475143))


if __name__ == '__main__':
    result = main()
    if result:
        pprint.pprint(result)

