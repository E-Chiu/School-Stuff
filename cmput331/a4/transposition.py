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
        if index == len(message) - 1 and row != len(key):
            # if message is not a square then add empty till it is
            for i in range(row, len(key)):
                mappingArr[i].append(None)

    # fill in cells
    index = 0
    for col in key:
        for row in range(len(mappingArr[0])):
            if mappingArr[col-1][row] != None:
                mappingArr[col-1][row] = message[index]
                index += 1

    decryptedMessage = ''
    # put the decrypted string back together
    col = 0
    row = 0
    for index in range(len(message)):
        if mappingArr[col][row] != None:
            decryptedMessage += mappingArr[col][row]
        col += 1
        if col == len(mappingArr):
            col = 0
            row += 1
        
    return decryptedMessage

def test():
    assert decryptMessage([4, 9, 3, 6, 2, 5, 10, 8, 1, 7], "dIcFbeJHaKG") == "abcdeFGHIJK"
    assert decryptMessage([19, 32, 38, 40, 47, 1, 31, 7, 16, 44, 35, 34, 15, 37, 46, 13, 45, 17, 27, 36, 24, 29, 3, 23, 48, 14, 11, 43, 5, 22, 25, 26, 33, 39, 30, 4, 20, 18, 21, 8, 41, 9, 12, 10, 42, 2, 50, 28, 49, 6], "c3ptu31m ") == "cmput 331"
    assert decryptMessage([2, 9, 10, 5, 6, 8, 4, 1, 3, 7], "993377668811552220044") == "290568413729056841372"
    assert decryptMessage([3, 5, 8, 7, 2, 1, 6, 9, 10, 4], "1627\n\n38\n\n05\n\n49\n\n\n") == "0\n1\n2\n3\n4\n5\n6\n7\n8\n9"
    assert decryptMessage([5, 2, 3, 4, 1], "   ab    ") == "  a    b "
    assert decryptMessage([162, 54, 148, 33, 155, 118, 172, 58, 52, 45, 125, 19, 126, 190, 44, 47, 32, 21, 195, 191, 86, 96, 108, 68, 80, 83, 201, 98, 156, 121, 176, 101, 143, 5, 104, 55, 48, 70, 149, 2, 1, 212, 28, 159, 7, 124, 77, 117, 184, 90, 81, 60, 24, 37,
56, 165, 73, 217, 85, 187, 34, 220, 30, 40, 95, 183, 153, 26, 69, 163, 204, 10, 206, 46, 76, 89, 202, 133, 123, 134, 110, 192, 64, 198, 189, 116, 94, 75, 139, 25, 66, 53, 186, 200, 20, 145, 150, 168, 112, 106, 177, 142, 129, 50, 178, 218, 97, 199, 158, 16, 147, 171, 13, 122, 82, 22, 72, 137, 23, 42, 111, 181, 216, 59, 170, 102, 15, 107, 113, 179, 213, 8, 197, 62, 71, 174, 194, 130, 115, 51, 63, 11, 167, 196, 210, 154, 29, 9, 209, 78, 221, 151, 173, 27, 84, 166, 207, 214, 39, 169, 74, 65, 49, 119, 61, 193, 57, 6, 88, 87, 211, 185, 35, 140, 103, 38, 164, 203, 36, 131, 161, 146, 219, 31, 152, 67, 188, 105, 43, 92, 3, 41, 215, 208, 136, 120, 17, 144, 182, 14, 99, 100, 18, 127, 175, 91, 205, 79, 93, 160, 180, 109, 4, 157, 132, 12, 138, 135, 141, 128,
114], "ruRaltf geys -LgelB.t  aopie.35.ntoi1Unrncdbn   Ial' mitn eufia. norofud,d.laehsTei0eq ke  yhnlecrmttnpti oyyiea4.s2a rRepn itanmirMaeo3pl aon.ksb.toanBp inlanla o h[C vecaa Pe dtnr eo ]acdfmyrum  d!oolayyt,r p] i1hsin psdaifelainncy hsg dys ce[o erc. ,i?rs Bn0n3. z Batu0  erch ,sg. a3Sm amdui. pezs. iJr isnk'h 7  su, aa 5 seo2, npeGu oa2tarlvgc.r,sNliiaadar aoie\ngdpyir53 ,re onr.siytsfolodves6s  3wedl leecn i gCaaegw auHt  Nlen eraaau") == "The opening is now considered inferior to 3.Bb5, the Ruy Lopez, and 3.Bc4, the Italian Game, and is accordingly rarely seen today at any level of play.\nMagnus Carlsen used it for a victory in 2013.[1] Black's main responses are 3...Nf6, leading to quiet play, and 3...d5, leading to sharp play. Ponziani's countergambit 3...f5!? was successfully played in the grandmaster game Hikaru Nakamura-Julio Becerra Rivero, US Championship 2007.[2]"
    decryptMessage([66, 71, 100, 23, 97, 55, 29, 50, 74, 82, 64, 27, 51, 78, 1, 61, 72, 28, 35, 6, 98, 52, 79, 59, 34, 25, 86, 31, 99, 85, 41, 13, 76, 58, 9, 46, 84, 57, 12, 87, 36, 56, 39, 26, 20, 70, 92, 89, 24, 15, 8, 7, 22, 10, 3, 2, 17, 88, 42, 19, 60, 5, 63, 18, 45, 91, 4, 81, 43, 48, 53, 38, 62, 67, 21, 65, 96, 94, 77, 44, 73, 30, 80, 69, 68, 95, 93, 32, 14, 90, 40, 16, 49, 83, 75, 47, 11, 33, 37, 54], "CMPUT 331!") == "C 133!PMTU"


from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
