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
Problem 2
"""

from sys import flags
import numpy as np
import re
def evalDecipherment(text1: str, text2: str) -> [float, float]:
    """
    docstring
    """
    # remove non alphabet characters
    text1 = re.sub("[^a-z]", "", text1)
    text2 = re.sub("[^a-z]", "", text2)
    # make uppercase so it is case insensitive
    text1 = text1.upper()
    text2 = text2.upper()

    keyAcc = 0
    deciphermentAcc = 0
    mapping = {}
    for index in range(len(text1)):
        if text1[index] == text2[index]:
            # if matching add to deciphermentAcc
            deciphermentAcc += 1
        # if not mapped yet add to map
        if text1[index] not in mapping:
            mapping[text1[index]] = text2[index]
    # check for key accuracy
    for key, value in mapping.items():
        if key == value:
            keyAcc += 1
    # return results
    return [(keyAcc/len(mapping)),(deciphermentAcc/len(text1))]



def test():
    "Run tests"
    np.testing.assert_array_almost_equal(evalDecipherment("this is an example", "tsih ih an ezample") , [0.7272727272727273, 0.7333333333333333])
    np.testing.assert_almost_equal(evalDecipherment("the most beautiful course is 331!", "tpq munt bqautiful cuurnq in 331!") , [0.7142857142857143, 0.625])
if __name__ == '__main__' and not flags.interactive:
    test()
