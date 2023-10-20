#!/usr/bin/env python3

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
Problem 2
"""

from sys import flags

def keyScore(mapping: dict, ciphertext: str, frequencies: dict, n: int) -> float:
    # try to decipher with mapping
    plaintext = ""
    for letter in ciphertext:
        if not letter.isalpha():
            plaintext += letter
        else:
            # get value from mapping and add to plaintext
            plaintext += mapping[letter]
    
    # get counts of ngrams
    ngramDict = {}
    # keep looping while we can still get a n sized ngram
    index = 0
    while index + n <= len(plaintext):
        ngram = plaintext[index:index+n]
        if ngram not in ngramDict:
            ngramDict[ngram] = 1
        else:
            ngramDict[ngram] += 1
        index += 1

    # calculate the ngram score
    ngramScore = 0
    for key, value in ngramDict.items():
        # only calculate if n gram is in freqs
        if key in frequencies:
            keyScore += value * frequencies[key]
    
    return ngramScore

  

def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking

if __name__ == "__main__" and not flags.interactive:
    test()





