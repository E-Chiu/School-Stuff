#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2023 <EthanChiu>
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
CMPUT 331 Assignment 2 Student Solution
September 2023
Author: Ethan Chiu
"""

import math

def encryptMessage(key: int, message: str):
    encryptedArr = [''] * key

    # go up and down the string and place the the letters in their respective column
    index = 0
    while True:
        for col in range(key):
            if index >= len(message):
                return ''.join(encryptedArr)
            encryptedArr[col] += message[index]
            index += 1
        for col in range(key - 2, 0, -1):
            if index >= len(message):
                return ''.join(encryptedArr)
            encryptedArr[col] += message[index]
            index += 1


def decryptMessage(key: int, message: str):
    # create an empty 2d array to map the correct placements of the letters
    mappingArr = [[] for i in range(len(message))]
    for i in range(len(message)):
        for j in range(key):
            mappingArr[i] += '_'

    # go up and down the string and place the the X where a letter should be for future reference
    direction = 1
    row = 0
    for i in range(len(message)):
        mappingArr[i][row] = 'X'

        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    
    # loop over the encryped message and replace X's with letters
    letterIndex = 0
    for row in range(key):
        for col in range(len(message)):
            if mappingArr[col][row] == 'X':
                mappingArr[col][row] = message[letterIndex]
                letterIndex += 1
    
    # loop one last time and put it all together
    finalMessage = ''
    direction = 1
    row = 0
    for i in range(len(message)):
        finalMessage += mappingArr[i][row]

        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    return finalMessage

def test():
    assert decryptMessage(2, encryptMessage(2, "SECRET")) == "SECRET"
    assert decryptMessage(3, encryptMessage(3, "CIPHERS ARE FUN")) == "CIPHERS ARE FUN"
    assert decryptMessage(4, encryptMessage(4, "HELLO WORLD")) == "HELLO WORLD"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
