#!/usr/bin/python3

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
CMPUT 331 Assignment 2 Student Solution
September 2023
Author: <Your name here>
"""

def encryptMessage(key: int, message: str):
    encryptedArr = [''] * key

    # split split the string in a loop into 3 different substrings then combine them at the end
    for col in range(key):
        for letter in range(col, len(message), key):
            encryptedArr[col] += message[letter];
    return ''.join(encryptedArr)


def decryptMessage(key: int, message: str):
    decryptedArr = []

    # split split the string in a loop into 3 different substrings then combine them at the end
    decryptedArr.append(message[0])
    for i in range(1, len(message)):
        index = (len(message) - 1) % (i * key)
        decryptedArr.append(message[index])
    return ''.join(decryptedArr)

def test():
    print(encryptMessage(2, "SECRET"))
    print(decryptMessage(2, "SCEERT"))
    assert decryptMessage(2, encryptMessage(2, "SECRET")) == "SECRET"
    assert decryptMessage(3, encryptMessage(3, "CIPHERS ARE FUN")) == "CIPHERS ARE FUN"
    assert decryptMessage(4, encryptMessage(4, "HELLO WORLD")) == "HELLO WORLD"

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
