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
Enhanced substitution cipher solver.
"""

import re, simpleSubCipher, simpleSubHacker

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def hackSimpleSub(message: str):
    """
    Simple substitution cipher hacker.
    First runs the textbook program to get an initial, potentially incomplete decipherment.
    Then uses regular expressions and a dictionary to decipher additional letters.
    """
    
    # Run the first pass
    # This Section of code taken from simpleSubHacker.py
    ciphertext = message
    letterMapping = simpleSubHacker.hackSimpleSub(message)
    
    # First create a simple sub key from the letterMapping mapping:
    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            # If there's only one letter, add it to the key.
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            message = message.replace(cipherletter.lower(), '_')
            message = message.replace(cipherletter.upper(), '_')
    key = ''.join(key)

    # With the key we've created, decrypt the ciphertext:
    firstPass = simpleSubCipher.decryptMessage(key, message)

    # find the indexes of all underscores
    cipherWords = ciphertext.split(' ')
    firstPassWords = firstPass.split(' ')

    unknownWords = {}
    for wordIndex in range(len(firstPassWords)):
        # if a word has a missing letter get its ciphertext character and put it in a dictionary
        word = firstPassWords[wordIndex]
        if '_' in word:
            for letterIndex in range(len(word)):
                letter = word[letterIndex]
                if letter == '_':
                    cipherChar = cipherWords[wordIndex][letterIndex]
                    if cipherChar in unknownWords:
                        unknownWords[cipherChar].append(word)
                    else:
                        unknownWords[cipherChar] = [word]

    dictFile = open("dictionary.txt", "r")
    dictionary = dictFile.read()
    dictionary = dictionary.replace("\n", " ")

    for cipherKey, cipherValue in unknownWords.items():
        matches = []
        possibleLetters = {}
        # for every missing word run a regex and get all possible matches
        for word in cipherValue:
            # remove underscores and non alphanumeric characters
            strippedWord = re.sub(r'\W+', '', word)
            strippedWord = strippedWord.replace("_", "\w{1}")
            matches = re.findall(r"(?i)\b" + strippedWord + r"\b", dictionary)
            for match in matches:
                # isolate the possible letter
                index = word.find('_')
                possibleLetter = match[index]
                search = re.search(possibleLetter, firstPass)
                if search == None:
                    # only add if it is not already mapped
                    if possibleLetter in possibleLetters:
                            possibleLetters[possibleLetter].append(match)
                    else:
                            possibleLetters[possibleLetter] = [match]
        # the letter with most entries is the real letter
        max = 0
        for plainKey, plainValue in possibleLetters.items():
            if len(plainValue) > max:
                letter = plainKey
                max = len(plainValue)
        index = LETTERS.find(letter.upper()) + 1
        # add letter to key
        if key[index] == "x":
            key = key[:index] + cipherKey.upper() + key[index + 1:]
    return




def test():
    # Provided test.
    message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'
    print(hackSimpleSub(message))
    # End of provided test.
    

if __name__ == '__main__':
    test()

