# Affine and Transposition Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

import detectEnglish, caesar, affine, transposition, itertools

SILENT_MODE = False

def hack(ciphertext, mode):

    if mode == "t":
        # try decoding with transposition
        for i in range(1, 9):
            perms = list(itertools.permutations(list(range(1,i+1))))
            for amount in range(100, 10, -5):
                for perm in perms:
                    decrypted = transposition.decryptMessage(perm, ciphertext)
                    if detectEnglish.isEnglish(decrypted, amount):
                        print(decrypted)

    if mode == "a":
        # try decoding with affine
        for key in range(len(affine.SYMBOLS) ** 2):
            keyA = affine.getKeyParts(key)[0]
            decrypted = affine.affine(key, ciphertext)
            if detectEnglish.isEnglish(decrypted, 50):
                return decrypted

    if mode == "c":
        # try decoding with caesar
        dictionary = open("dictionary.txt", "r")
        for word in dictionary:
            word = word.rstrip('\n')
            decrypted = caesar.decrypt(ciphertext, word)
            if detectEnglish.isEnglish(decrypted, 50):
                return decrypted

    return "nothing"

def main():
    cipherTexts = open("ciphers_version2.txt", "r")
    #outputFile = open("a4.txt", "w")

    # for transposition lines 3 4 and 8 for whatever reason I had to copy the lines straight from the txt and return every possible solution
    # decrypted = hack("Jacneiyp ydan nvr ieloeenmrht iorplmdbohanaailhrd hdioecc.aliayloe ctcu Jvac rstnyctreevpt tacloe  rn  uaeas ul uatrapas c ittet oyatmngef rgp iu", "t")

    # this worked fine for caesar and affine
    counter = 1
    for line in cipherTexts:
            line = line.rstrip('/n')
            decrypted = hack(line, "a")
            print(str(counter) + " " + decrypted)
            counter += 1
            #outputFile.write(decrypted)

if __name__ == '__main__':
    main()