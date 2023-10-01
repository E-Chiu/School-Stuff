#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2023 <Ethan Chiu>
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
#---------------------------------------------------------------

"""
CMPUT 331 Assignment 3 Student Solution
September 2023
Author: Ethan Chiu
"""

def crack_rng(m, sequence):
    r2, r3, r4, r5, r6 = tuple(sequence)
    # using equations:
    # eq1: R6 = aR5 + bR4 + c (mod m)
    # eq2: R5 = aR4 + bR3 + c (mod m)
    # eq3: R4 = aR3 + bR2 + c (mod m)

    # first subtract the variables from each other to remove c
    # eq4 = eq1 - eq3
    eq4 = r6 - r4
    aCoeff4 = r5 - r3
    bCoeff4 = r4 - r2
    # eq5 = eq2 - eq3
    eq5 = r5 - r4
    aCoeff5 = r4 - r3
    bCoeff5 = r3 - r2

    # since the denominator can be crossed out we can cross multiply in advance to avoid working with decimals
    # eq6 = eq4 * bCoeff5
    eq6 = eq4 * bCoeff5
    aCoeff6 = aCoeff4 * bCoeff5
    # eq7 = eq5 * beCoeff4
    eq7 = eq5 * bCoeff4
    aCoeff7 = aCoeff5 * bCoeff4

    # subtract the equations to single out b
    # eq 8 = eq6 - eq 7
    eq8 = eq6 - eq7
    aCoeff8 = aCoeff6 - aCoeff7
    
    # find the modular inverse of a
    aInv = pow(aCoeff8, -1, m)
    # find a
    a = (eq8 * aInv) % m

    # plug back into the eqation to find b
    # plug into eq4
    eq4 = eq4 - (aCoeff4 * a)

    # find inverse of b
    bInv = pow(bCoeff4, -1, m)
    #find b
    b = (eq4 * bInv) % m

    # plug back into the eqation to find c
    # plug into eq1
    eq1 = r6 - (a * r5 + b * r4)
    # find c
    c = eq1 % m

    # return the vars
    return [a, b, c]

def test():
    assert crack_rng(17, [14, 13, 16, 3, 13]) == [3, 5, 9]
    assert crack_rng(9672485827, [4674207334, 3722211255, 3589660660, 1628254817, 8758883504]) == [22695477, 77557187, 259336153]
    assert crack_rng(101, [0, 91, 84, 16, 7]) == [29, 37, 71]
    assert crack_rng(222334565193649,[438447297,50289200612813,17962583104439,47361932650166,159841610077391]) == [1128889, 1023, 511]

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()