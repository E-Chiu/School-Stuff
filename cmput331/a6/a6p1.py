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
Problem 1
"""

from sys import flags

def ngramsFreqsFromFile(textFile: str, n: int) -> dict:
    """
    textFile: 'wells.txt'
    """
    # open textfile
    textDoc = open(textFile, "r")
    textText = textDoc.read()

    ngramDict = {}
    # get the counts of the ngram first
    # keep looping while we can still get a n sized ngram
    index = 0
    total = 0
    while index + n <= len(textText):
        # increment the count of the ngram
        ngram = textText[index:index+n]
        if ngram not in ngramDict:
            ngramDict[ngram] = 1
            total += 1
        else:
            ngramDict[ngram] += 1
            total += 1
        index += 1
    
    # calculate relative freq of the ngrams
    for key, value in ngramDict.items():
        ngramDict[key] = value / total
    
    return ngramDict




def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    returnDict = ngramsFreqsFromFile("wells.txt", 1)
    total = 0
    for key, value in returnDict.items():
        total += value
    assert(total > 0.9)
    assert(total < 1.1)

    returnDict = ngramsFreqsFromFile("wells.txt", 3)
    total = 0
    for key, value in returnDict.items():
        total += value
    assert(total > 0.9)
    assert(total < 1.1)

    returnDict = ngramsFreqsFromFile("wells.txt", 5)
    total = 0
    for key, value in returnDict.items():
        total += value
    assert(total > 0.9)
    assert(total < 1.1)


if __name__ == "__main__" and not flags.interactive:
    test()
