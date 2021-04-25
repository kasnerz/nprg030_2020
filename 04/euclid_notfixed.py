#!/usr/bin/env python3

# TODO: fix

# spočítá nejvyššího společného dělitele čísel a,b
def euclid_gcd(a, b):
    while a > 0:
        a = a % b

        if a == 1:
            return a

    return b

# testy
assert(euclid_gcd(10,2) == 2)
assert(euclid_gcd(10,5) == 5)
assert(euclid_gcd(7,7) == 7)
assert(euclid_gcd(7,3) == 1)