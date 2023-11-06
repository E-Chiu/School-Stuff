#!/usr/bin/env python3

# ---------------------------------------------------------------
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
# ---------------------------------------------------------------

"""
Assignment 7 Problem 1
"""

from sys import flags
import util

NUM_SYM = 26

# This function was taken from the eclass example
def vigenere(key, message, mode):
    translated = [] 
    keyIndex = 0
    key = key.upper()

    for symbol in message: 
        num = util.let2ind(symbol.upper())
        if (num < 0) or (num >= NUM_SYM):
            translated.append(symbol)
        else:
            if mode == 'encrypt':
                num = num + util.let2ind(key[keyIndex])
            elif mode == 'decrypt':
                num = num - util.let2ind(key[keyIndex])

            nextLetter = util.ind2let(num % NUM_SYM)
            if symbol.isupper():
                translated.append(nextLetter)
            elif symbol.islower():
                translated.append(nextLetter.lower())

            keyIndex = (keyIndex + 1) % len(key)

    return ''.join(translated)

def antiKasiski(key: str, plaintext: str):
    """
    Thwart Kasiski examination 
    """
    # encrypt the first time
    encrypted = vigenere(key, plaintext, "encrypt")
    index = 0
    while index < len(plaintext):
        # get first 3 characters
        ngram = encrypted[index:index+3]
        if encrypted[index:].count(ngram) > 1:
            # if ngram is in the ciphertext more than once add an x
            plaintext = plaintext[:index+3] + "X" + plaintext[index+3:]
            # encrypt with changes
            encrypted = vigenere(key, plaintext, "encrypt")
            # jump index up
            index += 4
        else:
            #move up normally
            index += 1
    return vigenere(key, plaintext, "encrypt")

def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    assert antiKasiski('WICK', 'THOSEPOLICEOFFICERSOFFEREDHERARIDEHOMETHEYTELLTHEMAJOKETHOSEBARBERSLENTHERALOTOFMONEY') == 'PPQCAXQVEKGYBNZSYMTCTWHPAZGNDMTKNQFODWOOPPGHUBGVHBJOTUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU'
    assert antiKasiski("WICK", "ABCDABCD") == 'WJEHZIDMZ'

# Invoke test() if called via `python3 a7p1.py`
# but not if `python3 -i a7p1.py` or `from a7p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()
