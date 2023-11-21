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

def getPrime(n):
    primes = []

    for num in range(2, n):
        for i in range(2, num):
            if num%i == 0:
                # if another number divides it break out
                break
        else:  
            primes.append(num)
    return primes

def getFactors(primes, n):
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            if primes[i] * primes[j] == n:
                p = primes[j]
                q = primes[i]
                return p, q

def finitePrimeHack(t: int, n: int, e: int) -> Tuple[int, int, int]:
    """
    Hack RSA assuming there are no primes larger than t
    """
    # get prime numbers
    primes = getPrime(t)
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
    # This function is ignored in our marking


# Invoke test() if called via `python3 a9p1.py`
# but not if `python3 -i a9p1.py` or `from a9p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()
