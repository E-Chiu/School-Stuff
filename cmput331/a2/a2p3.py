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
CMPUT 331 Assignment 2 Student Solution
September 2023
Author: Ethan Chiu
"""

from typing import List

def decryptMessage(key: List[int], message: str):
    mappingArr = [[] for i in range(len(key))]

    # add Xs to spots where letters would have been
    row = 0
    for index in range(len(message)):
        mappingArr[row] += 'X'
        row += 1
        if row == len(key):
            row = 0

    # loop through the message place the letters into their columns
    index = 0
    for col in range(len(key)):
        for row in range(len(mappingArr[col])):
            mappingArr[col][row] = message[index]
            index += 1

    # order the array based off the key
    decryptArr = [[] for i in range(len(key))]
    index = 0
    for col in key:
        decryptArr[col - 1] = mappingArr[index]
        index += 1

    decryptedMessage = ''
    # put the decrypted string back together
    col = 0
    row = 0
    for index in range(len(message)):
        decryptedMessage += decryptArr[col][row]
        col += 1
        if col == len(decryptArr):
            col = 0
            row += 1
        
    return decryptedMessage

def test():
    assert decryptMessage([2, 4, 1, 5, 3], "IS HAUCREERNP F") == "CIPHERS ARE FUN"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
