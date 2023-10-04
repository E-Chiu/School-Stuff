# Affine and Transposition Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

import detectEnglish, caesar, affine, transposition, itertools

SILENT_MODE = False

def hack(ciphertext):

    # try decoding with transposition
    perms = list(itertools.permutations([1,2,3,4,5,6,7,8,9,10]))
    for perm in perms:
        decrypted = transposition.decryptMessage(perm, ciphertext)
        if detectEnglish.isEnglish(decrypted, 60):
            return decrypted

    # try decoding with affine
    for i in range(26):
        decrypted = affine.affine(i, ciphertext)
        if detectEnglish.isEnglish(decrypted, 60):
            return decrypted

    # try decoding with caesar
    dictionary = open("dictionary.txt", "r")
    for word in dictionary:
        word = word.rstrip('\n')
        decrypted = caesar.decrypt(ciphertext, word)
        if detectEnglish.isEnglish(decrypted, 60):
            return decrypted
        

    return "nothing"
    if cipherType == 'caesar':
        keyRange = range(caesar.NUM_SYM)
    elif cipherType == 'transposition':
        keyRange = range(1,len(ciphertext))
    elif cipherType == 'affine':
        keyRange = range(len(affine.SYMBOLS) ** 2)

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
    outPutFile = open("a4.txt", "w")

    for line in cipherTexts:
            line = line.rstrip('/n')
            decrypted = hack(line)
            print(decrypted)
            #outPutFile.write(decrypted)

if __name__ == '__main__':
    main()