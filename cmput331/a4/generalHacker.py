# Affine and Transposition Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

import cryptomath, detectEnglish, caesar, affine, transposition, itertools

SILENT_MODE = False

def hack(ciphertext):

    # try decoding with transposition
    for amount in range(100, 10, -10):
        for i in range(1,10):
            perms = list(itertools.permutations(list(range(1,i+1))))
            for perm in perms:
                decrypted = transposition.decryptMessage(perm, ciphertext)
                if detectEnglish.isEnglish(decrypted, amount):
                    return "transposition: "  + decrypted
            
    return "nothing"

"""
    # try decoding with affine
    for key in range(len(affine.SYMBOLS) ** 2):
        keyA = affine.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affine.SYMBOLS)) != 1:
            continue
        decrypted = affine.affine(key, ciphertext)
        if detectEnglish.isEnglish(decrypted, 50):
            return "affine: " + decrypted

    # try decoding with caesar
    dictionary = open("dictionary.txt", "r")
    for word in dictionary:
        word = word.rstrip('\n')
        decrypted = caesar.decrypt(ciphertext, word)
        if detectEnglish.isEnglish(decrypted, 50):
            return "caesar: " + decrypted

    return "nothing"
"""

"""
    for key in keyRange:
        if cipherType == 'caesar':
            decrypted = caesar.caesar(key, ciphertext)
        elif cipherType == 'transposition':
            decrypted = transposition.decryptMessage(key, ciphertext)
        elif cipherType == 'affine':
            keyA = affine.getKeyParts(key)[0]
            if cryptomath.gcd(keyA, len(affine.SYMBOLS)) != 1:
                continue
            decrypted = affine.affine(key, ciphertext, 'decrypt')
"""

def main():
    cipherTexts = open("ciphers_version2.txt", "r")
    outputFile = open("a4.txt", "w")

    for line in cipherTexts:
            line = line.rstrip('/n')
            decrypted = hack(line)
            print(decrypted)
            #outputFile.write(decrypted)

if __name__ == '__main__':
    main()