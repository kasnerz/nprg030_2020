#!/usr/bin/env python3

# TODO: fix

# vrátí seznam prvočísel menších nebo rovných n
def eratosthenes(n):
    primes = []

    for i in range(2, n):
        is_prime = True

        for p in primes:
            if i % p == 0:
                is_prime = False

        if is_prime:
            primes.append(i)

    return primes

# testy
assert(eratosthenes(1) == [])
assert(eratosthenes(4) == [2, 3])
assert(eratosthenes(15) == [2, 3, 5, 7, 11, 13])