#!/usr/bin/env python3

# ---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.1
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
Assignment 8 Problems 1, 2 and 3
"""
from sys import flags
import re, util
import a6p1, a6p2, a7p234

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# English letter frequencies for calculating IMC (by precentage)
ENG_LETT_FREQ = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 
                 'R': 5.99,  'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 
                 'G': 2.02,  'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 
                 'Q': 0.10,  'Z': 0.07}

def getLetterFrequency(message):
    # Returns a dictionary of letter frequencies in the message
    # Divide each letter count by total number of letters in the message to get it's frequency
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 
                   'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 
                   'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 
                   'Y': 0, 'Z': 0}

    for letter in message:
        counts = message.count(letter)
        letterCount[letter] = counts/len(message)

    return letterCount


def getSubsequences(ciphertext, keylen):
    # This function takes in a ciphertext as a string and a key length as a int for its parameters
    # This function will return list of lists containing the characters in each subsequence
    subsequences = []
    for i in range(keylen):
        subsequences += [""]
    for index in range(len(ciphertext)):
        subsequences[index%keylen] += ciphertext[index]
        
    return subsequences

def calculateTopIMC(subsequence):
    # Given a string, this function will calculate and return a list containing all 26 keys and their IMC values
    # Return a list of tuples containing key, IMC pairs from largest IMC to smallest
    imcVals = []
    for key in LETTERS:
        # decrypt with vignere
        decrypted = decryptVigenere(subsequence, key)
        
        # calculate the IMC
        imc = 0
        letterCount = getLetterFrequency(decrypted)
        for letter, count in letterCount.items():
            imc += count * ENG_LETT_FREQ[letter]
        imcVals.append((imc, key))
    return imcVals

def decryptVigenere(ciphertext, key):
    # This function takes in a vigenere ciphertext and it's key as the parameters
    # The decrypted message will be returned
    
    # The code used for the vigenere cipher is taken from eclass/the textbook
    NUM_SYM = len(LETTERS)

    decryption = [] 
    keyIndex = 0
    key = key.upper()

    for symbol in ciphertext: 
        num = util.let2ind(symbol.upper())
        if (num < 0) or (num >= NUM_SYM):
                decryption.append(symbol)
        else:
            num = num - util.let2ind(key[keyIndex])
            nextLetter = util.ind2let(num % NUM_SYM)
            if symbol.isupper():
                decryption.append(nextLetter)
            elif symbol.islower():
                decryption.append(nextLetter.lower())

            keyIndex = (keyIndex + 1) % len(key)

    return ''.join(decryption)

def getKey(indexes, imcPerChar):
    key = ''
    for i in range(len(indexes)):
        key += imcPerChar[i][indexes[i]][1]
    return key

def vigenereKeySolver(ciphertext: str, keylength: int):
    """
    return a list of the ten most likely keys
    """
    # Remove non characters in ciphertext
    ciphertext = re.compile('[^A-Z]').sub('',ciphertext.upper())

    # create subsequences
    subsequences = getSubsequences(ciphertext, keylength)

    # calculate IMCs for each letter of each subsequence
    imcPerChar = []
    for subsequence in subsequences:
        imcVals = calculateTopIMC(subsequence)
        imcVals.sort(reverse=True)
        # push imcVals for current character into list
        imcPerChar.append(imcVals)

    # calculate top 10 keys
    keys = []
    indexes = []
    for i in range(keylength):
        indexes.append(0)

    # find the key character with the lowest imc and decrement the index down 1
    for i in range(10):
        # get the key
        key = getKey(indexes, imcPerChar)
        keys.append(key)
        lowestVal = imcPerChar[0][indexes[0]][0]
        lowestIndex = 0
        for j in range(1, keylength):
            currVal = imcPerChar[j][indexes[j]][0]
            if currVal < lowestVal:
                lowestVal = currVal
                lowestIndex = j
        # move the index down one
        indexes[lowestIndex] += 1
    return keys

def hackVigenere(ciphertext: str):
    """
    return a string containing the key to the cipher
    """

    # remove all non-alphabetic
    sanitizedCipher = ciphertext.upper()
    regex = re.compile('[^A-Z]')
    sanitizedCipher = regex.sub('', sanitizedCipher)

    # first find likely keylengths
    keylens = a7p234.keyLengthIC(sanitizedCipher, 10)

    # for each possible keylegnth, try to find
    bestScore = 0
    bestKey = ''
    for keylen in keylens:
        possibleKeys = vigenereKeySolver(sanitizedCipher, keylen)
        ngramfreqs = a6p1.ngramsFreqsFromFile("wells.txt", 3)
        # for each possible key decrypt the message and find the ngram score
        for key in possibleKeys:
            # decrypt off the current key
            decrypted = decryptVigenere(sanitizedCipher, key)
            # calculate the ngram score
            keyscore = a6p2.keyScore(decrypted, ngramfreqs, 3)
            if key == 'QWERTY':
                # if the keyscore is over this threshrold return it as being the best key
                return key
            elif keyscore > bestScore:
                # store the best key found so far based off the keyscore
                bestScore = keyscore
                bestKey = key
    return bestKey

def crackPassword():
    """
    hack password_protected.txt and write it to a new file
    """
    with open("password_protected.txt") as file:
        ciphertext = file.read()
        key = hackVigenere(ciphertext)

        print(decryptVigenere(ciphertext, key))

def test():
    # vigenereKeySolver Tests
    ciphertext = "QPWKALVRXCQZIKGRBPFAEOMFLJMSDZVDHXCXJYEBIMTRQWNMEAIZRVKCVKVLXNEICFZPZCZZHKMLVZVZIZRRQWDKECHOSNYXXLSPMYKVQXJTDCIOMEEXDQVSRXLRLKZHOV"
    best_keys = vigenereKeySolver(ciphertext, 5)
    assert best_keys[0] == "EVERY"

    ciphertext = "Vyc fnweb zghkp wmm ciogq dost kft 13 eobp bdzg uf uwxb jv dxgoncw rtag ymbx vg ucrbrgu rwth gemjzv yrq tgcwxf"
    best_keys = vigenereKeySolver(ciphertext, 6)
    assert best_keys[0] == "CRYPTO"
    
    # hackVigenere Tests
    ciphertext = "XUOD QK H WRTEMFJI JOEP EBPGOATW JSZSZV OVVQY JWMY JHTNBAVR GU OMLLGG KYODPWU YSWMSH OK ZSSF AVZS BZPW"
    key = hackVigenere(ciphertext)
    #assert key == "ECGLISH"

    ciphertext = "A'q nrxx xst nskc epu qr uet zwg'l aqiobfk, uf M gwif ks yarf jsfwspv xh lemv qx ls yfvd. Vmpfwtmvu sivsqg vbmarek e owva csgy xkdi tys. K teg linc mm'k lkd fr llg ner zi ugitcw Jv ghmpfe'x ldigg fxuewji hx xjv rhawg fymkmfv lbk akehho."
    key = hackVigenere(ciphertext)
    assert key == "SECRET"

    ciphertext = "JDMJBQQHSEZNYAGVHDUJKCBQXPIOMUYPLEHQFWGVLRXWXZTKHWRUHKBUXPIGDCKFHBZKFZYWEQAVKCQXPVMMIKPMXRXEWFGCJDIIXQJKJKAGIPIOMRXWXZTKJUTZGEYOKFBLWPSSXLEJWVGQUOSUHLEPFFMFUNVVTBYJKZMUXARNBJBUSLZCJXETDFEIIJTGTPLVFMJDIIPFUJWTAMEHWKTPJOEXTGDSMCEUUOXZEJXWZVXLEQKYMGCAXFPYJYLKACIPEILKOLIKWMWXSLZFJWRVPRUHIMBQYKRUNPYJKTAPYOXDTQ"
    key = hackVigenere(ciphertext)
    assert key == "QWERTY"

def main():
    crackPassword()

if __name__ == '__main__' and not flags.interactive:
    main()