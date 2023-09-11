#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2023 Ethan Chiu
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
CMPUT 331 Assignment 1 Student Solution
September 2023
Author: Ethan Chiu
"""


import string
from sys import flags


LETTERS = ''.join([u+l for u, l in 
    zip(string.ascii_uppercase, string.ascii_lowercase)])


def get_map(letters=LETTERS):
    SHIFTDICT = {}
    LETTERDICT = {}

    # update the dictinaries with the letters and their corresponding shifts
    shift = 0
    for letter in LETTERS:
        SHIFTDICT.update({letter:shift})
        LETTERDICT.update({shift:letter})
        shift += 1
    
    return SHIFTDICT, LETTERDICT



def encrypt(message: str, key: str):
    # go through each character and apply the shift
    # code inspired from ceasarCipher.py
    output = ''
    i = 0
    for char in message:
        num = SHIFTDICT.get(char)
        if num != None:
            # only increment counters for the key if the character is encodable
            # find the corresponding character of the key
            keyIndex = (len(key) + i) % len(key)
            shift = SHIFTDICT.get(key[keyIndex])

            num = num + shift
            if num >= len(SHIFTDICT):
                num = num - len(SHIFTDICT)
            output = output + LETTERDICT.get(num)
            i += 1
        else:
            output = output + char
    return output
        

def decrypt(message: str, key: str):
# get the shift amount from the dict
    shift = SHIFTDICT.get(key)

    # go through each character and apply the shift
    # code inspired from ceasarCipher.py
    output = ''
    i = 0
    for char in message:
        num = SHIFTDICT.get(char)
        if num != None:
            # only increment counters for the key if the character is encodable
            # find the corresponding character of the key
            keyIndex = (len(key) + i) % len(key)
            shift = SHIFTDICT.get(key[keyIndex])

            num = num - shift
            if num < 0:
                num = num + len(SHIFTDICT)
            output = output + LETTERDICT.get(num)
            i += 1
        else:
            output = output + char
    return output

def test():
    global SHIFTDICT, LETTERDICT 
    SHIFTDICT, LETTERDICT = get_map()
    assert encrypt("AAA!AAA", "AaBb") == 'AaB!bAa'
    assert decrypt("AaB!bAa", "AaBb") ==  'AAA!AAA'

if __name__ == "__main__" and not flags.interactive:
    test()