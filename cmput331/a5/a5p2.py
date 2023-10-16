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
    # remove spaces
    text1 = text1.replace(' ', '')
    text2 = text2.replace(' ', '')
    # remove nonalphanumeric
    text1 = re.sub(r'\W+', '', text1)
    text2 = re.sub(r'\W+', '', text2)
    # make uppercase so it is case insensitive
    text1 = text1.upper()
    text2 = text2.upper()

    keyAcc = 0
    deciphermentAcc = 0
    uniques = []
    for index in range(len(text1)):
        if text1[index] != text2[index]:
            # if not matching add to deciphermentAcc regardless
            deciphermentAcc += 1
            if text1[index] not in uniques:
                # if not a recorded character yet add to counter and add to list
                keyAcc += 1
                uniques.append(text1[index])
    
    text1Unique = ''.join(set(text1))
    # return results
    return [1-(keyAcc/len(text1Unique)),1-(deciphermentAcc/len(text1))]



def test():
    "Run tests"
    np.testing.assert_array_almost_equal(evalDecipherment("this is an example", "tsih ih an ezample") , [0.7272727272727273, 0.7333333333333333])
    np.testing.assert_almost_equal(evalDecipherment("the most beautiful course is 331!", "tpq munt bqautiful cuurnq in 331!") , [0.7142857142857143, 0.625])
if __name__ == '__main__' and not flags.interactive:
    test()
