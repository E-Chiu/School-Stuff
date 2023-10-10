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
Subsititution cipher frequency analysis
"""
ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

from sys import flags
from collections import Counter # Helpful class, see documentation or help(Counter)
import re

def freqDict(ciphertext: str) -> dict:
    """
    Analyze the frequency of the letters
    """
    # count the characters
    stippedCipher = re.sub(r'\W+', '', ciphertext)
    counter = Counter(stippedCipher)
    letterCounts = counter.most_common()

    mapDict = {}
    index = 0
    for letter, count in letterCounts:
        # if it is the biggest number just apply mapping and move on
        if index == len(letterCounts) -1 or count > letterCounts[index + 1][1]:
            mapDict[letter] =  ETAOIN[index]
            index += 1
        else:
            tempList = []
            startIndex = index
            while letterCounts[index][1] > letterCounts[index + 1][1]:
                # add chars to list
                tempList.append(letterCounts[index])
                index += 1
            # sort alphabetically
            tempList = sorted(tempList)
            while startIndex > index:
                # pop from temp list and assign it to next letter
                mapDict[tempList.pop()] = ETAOIN[startIndex]
                startIndex += 1
    return mapDict

    

def freqDecrypt(mapping: dict, ciphertext: str) -> str:
    """
    Apply the mapping to ciphertext
    """
    plaintext = ''
    # loop through text and apply mapping
    for letter in ciphertext:
        if letter in mapping:
            translated = mapping[letter]
            if letter.isupper():
                plaintext += translated.upper()
            else:
                plaintext += translated.lower()
        else:
            plaintext += letter
    return plaintext



def test():
    "Run tests"
    assert type(freqDict("A")) is dict
    assert freqDict("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")["A"] == "E"
    assert freqDict("AABBA")['B'] == "T"
    assert freqDict("-: AB CD AH")['A'] == "E"
    assert freqDecrypt({"A": "E", "Z": "L", "T": "H", "F": "O", "U": "W", "I": "R", "Q": "D"}, "TAZZF UFIZQ!") == "HELLO WORLD!"


# Invoke test() if called via `python3 a5p1.py`
# but not if `python3 -i a5p1.py` or `from a5p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()
