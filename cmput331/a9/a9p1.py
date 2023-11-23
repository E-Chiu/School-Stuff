#!/usr/bin/env python3

# ---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2023 <<Insert your name here>>
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
# ---------------------------------------------------------------

"""
Assignment 9 Problem 1
"""

from sys import flags
from typing import Tuple
import math

def primeSieve(sieveSize):
     # Returns a list of prime numbers calculated using
     # the Sieve of Eratosthenes algorithm.

     sieve = [True] * sieveSize
     sieve[0] = False # Zero and one are not prime numbers.
     sieve[1] = False

     # Create the sieve:
     for i in range(2, int(math.sqrt(sieveSize)) + 1):
         pointer = i * 2
         while pointer < sieveSize:
             sieve[pointer] = False
             pointer += i

     # Compile the list of primes:
     primes = []
     for i in range(sieveSize):
         if sieve[i] == True:
             primes.append(i)

     return primes

def getFactors(primes, n):
    for prime in primes:
        factor = n/prime
        if factor in primes:
            q = prime
            p = int(factor)
            return p, q

def finitePrimeHack(t: int, n: int, e: int) -> Tuple[int, int, int]:
    """
    Hack RSA assuming there are no primes larger than t
    """
    # get prime numbers
    primes = primeSieve(t)
    primes.reverse()
    # find 2 largest prime factors
    p, q = getFactors(primes, n)
    d = e % ((p-1) * (q-1))
    d = pow(d, -1, (p-1) * (q-1))

    return (p, q, d)


def test():
    "Run tests"
    assert finitePrimeHack(100, 493, 5) == (17, 29, 269)
    assert finitePrimeHack(2**16,2604135181,1451556085) == (48533,53657, 60765)
    # TODO: test thoroughly by writing your own regression tests
    print(finitePrimeHack(2**14,160728233,8951))
    print(finitePrimeHack(2**14,106646587,14023))
    print(finitePrimeHack(2**14,255706897,9061))
    print(finitePrimeHack(2**14,167131319,8215))
    print(finitePrimeHack(2**14,186609961,11283))
    # This function is ignored in our marking


# Invoke test() if called via `python3 a9p1.py`
# but not if `python3 -i a9p1.py` or `from a9p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()
