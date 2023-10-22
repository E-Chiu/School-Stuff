#!/usr/bin/env python3

#---------------------------------------------------------------
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
#---------------------------------------------------------------

"""
Problem 4
"""

from sys import flags

import numpy as np
from a6p1 import ngramsFreqsFromFile
from a6p3 import bestSuccessor, LETTERS

ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

def decipherToFile(mapping, cipherText):
    # do the substitution
    plainText = ''
    for letter in cipherText:
        if letter not in mapping:
            plainText += letter
        else:
            plainText += mapping[letter]
    
    # write to file
    outputFile = open("text_plain.txt", "w")
    outputFile.write(plainText)

def getCipherFreqs(cipherText):
    freqs = {' ': 0}
    for letter in LETTERS:
        freqs[letter] = 0
    # get the counts of the letters
    for letter in cipherText:
        freqs[letter] += 1
    # get the freq
    for key, value in freqs.items():
        freqs[key] = value / len(cipherText)

    return freqs


def breakSub(cipherFile: str, textFile: str, n: int) -> None:
    """
    Inputs:
        cipherFile: 
            'text_finnegan_cipher.txt' for implementation
            'text_cipher.txt' for submission
        textFile: 'wells.txt'
    Outputs:
        'text_finnegan_plain.txt' for implementation
        'text_plain.txt' for submission
    """
    # open textfile
    cipherDoc = open(cipherFile, "r")
    cipherText = cipherDoc.read()

    # get the ngram freqs
    textFreqs = ngramsFreqsFromFile(textFile, n)
    
    cipherFreqs = getCipherFreqs(cipherText)

    # sort the frequencies
    keys = list(cipherFreqs.keys())
    values = list(cipherFreqs.values())
    sorted_value_index = np.argsort(values)
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

    # map sorted frequencies to etaoin
    mapping = {}
    index = 25
    for key, value in sorted_dict.items():
        if key == ' ':
            mapping[key] = ' '
        else:
            mapping[key] = ETAOIN[index]
            index -= 1

    oldMap = {}
    while True:
        # keep looping and finding successors
        bestMap = bestSuccessor(mapping, cipherText, textFreqs, n)
        if bestMap == oldMap:
            # once best map has been found apply the decipherment
            decipherToFile(bestMap, cipherText)
            return
        else:
            oldMap = bestMap

def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    breakSub("text_finnegan_cipher.txt", "wells.txt", 4)
    
if __name__ == "__main__" and not flags.interactive:
    test()