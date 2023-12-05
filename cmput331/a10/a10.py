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
Assignment 10
"""
from sys import flags
import string, glob
from collections import Counter

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#https://www.geeksforgeeks.org/python-remove-punctuation-from-string/
#https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index

def cliSSD(ciphertext: str, files):
    """
    Args:
        ciphertext (str)
        files (list of str)
    Returns:
        dict
    """
    returnDict = {}
    # get ssd for ciphertext
    cipherSSD = []
    for letter in LETTERS:
        freq = ciphertext.count(letter)/len(ciphertext)
        cipherSSD.append(freq)
    cipherSSD.sort()
  
    for file in files:
        with open(file) as f:
            #get ssd for current file
            fileText = f.read().upper()
            fileSSD = []
            for letter in LETTERS:
                freq = fileText.count(letter)/len(fileText)
                fileSSD.append(letter, freq)
            fileSSD.sort()
        # compute the difference
        SSDDiff = 0
        for i in range(len(LETTERS)):
            SSDDiff = (cipherSSD[i] - fileSSD[i])**2
        returnDict[file] == SSDDiff
    return returnDict


def cliDPD(ciphertext: str, files):
    """
    Args:
        ciphertext (str)
        files (list of str)
    Returns:
        dict
    """
    returnDict = {}
    # get ddpd for ciphertext
    cipherDPD = {}
    for word in ciphertext:
        # remove punctuation
        word = word.translate(str.maketrans('', '', string.punctuation))
        letterCounts = Counter(word)
        DPDTuple = []
        # get counts of letters and put into tuples
        for key, val in letterCounts.items():
            DPDTuple.append(val)
        DPDTuple.sort(reverse=True)
        DPDTuple = tuple(DPDTuple)
        # add to dictionary
        if DPDTuple in cipherDPD:
            cipherDPD[DPDTuple] += 1
        else:
            cipherDPD[DPDTuple] = 1
  
    for file in files:
        with open(file) as f:
            #get dpd for current file
            fileText = f.read().upper()
            for word in fileText:
                # remove punctuation
                word = word.translate(str.maketrans('', '', string.punctuation))
                letterCounts = Counter(word)
                fileDPD = {}
                DPDTuple = []
                # get counts of letters and put into tuples
                for key, val in letterCounts.items():
                    DPDTuple.append(val)
                DPDTuple.sort(reverse=True)
                DPDTuple = tuple(DPDTuple)
                # add to dictionary
                if DPDTuple in fileDPD:
                    fileDPD[DPDTuple] += 1
                else:
                    fileDPD[DPDTuple] = 1
            # compute the difference
            DPDDiff = 0
            for key, val in fileDPD:
                if key in cipherDPD:
                    DPDDiff = (cipherDPD[key] - fileDPD[key])**2
            returnDict[file] == DPDDiff
    return returnDict

def cliSSDTest(ciphertext_files, sampletext_files):
    """
    Args:
        ciphertext_files (list of str)
        sampletext_files (list of str)
    Returns:
        dict
    """
    matchedDict = {}
    for cipherFile in ciphertext_files:
        f = open(cipherFile, encoding="utf8")
        ciphertext = f.read()
        # calculate the ssd
        ssdDict = cliSSD(ciphertext, sampletext_files)
        for key, value in ssdDict:
            # store them in (ciphertext, value) tuples to keep track of best ciphertext
            if key not in matchedDict:
                matchedDict[key] == (ciphertext, value)
            elif matchedDict[key][1] < value:
                # if matches better replace in dict
                matchedDict[key] = (ciphertext, value)
    
    for key, value in matchedDict:
            # remove the tuple
            matchedDict[key] = value[0]
    return matchedDict


def cliDPDTest(ciphertext_files, sampletext_files):
    """
    Args:
        ciphertext_files (list of str)
        sampletext_files (list of str)
    Returns:
        dict
    """
    raise NotImplementedError()


def test():
    ciphertext_files = glob.glob("texts\\ciphertext*.txt")
    sampletext_files = glob.glob("texts\\sample_*.txt")

    cliSSDTest(ciphertext_files, sampletext_files)


if __name__ == "__main__" and not flags.interactive:
    test()