def getInputFile(wasError):
    """
    gets name of file from user
    """
    # call this function until input is correct format
    if wasError:
        fileName = input("Invalid filename extension. please re-enter the input filename:")
    else:
        fileName = input("Enter the input filename:")
    if fileName[-4:] != ".txt":
        getInputFile(True)
    return fileName

def decrypt(fileName):
    """
    reads lines from file and decrypts message using key
    """
    lines = []
    tempFile = open(fileName, 'r')
    lines = tempFile.readlines()
    # seperate the key and cipher
    key, word = lines[0], lines [1]
    # remove any leading/trailing whitespace from key and cipher
    key = int(key.strip())
    # remove multiples of 26 from the key
    key = key % 26
    word = word.lower().strip()
    splitWord = list(word)
    decryptedWord = []
    # subtract the key from the ascii number
    for char in splitWord:
        beforeUni = ord(char)
        afterChar = chr(beforeUni)
        # if the subtracting goes past a, loop around
        if beforeUni - key < ord('a') and beforeUni != ord(' '):
            afterChar = chr((ord('z') + 1) - (key - (beforeUni - ord('a'))))
            beforeUni = (ord('z') + 1) - (key - (beforeUni - ord('a')))
        elif beforeUni != ord(' '):
            afterChar = chr(beforeUni - key)
        decryptedWord.append(afterChar)
    finalWord = ''.join(decryptedWord)
    return finalWord

def main():
    """
    main function that calls other functions
    """
    fileName = getInputFile(False)
    finalWord = decrypt(fileName)
    print('The decrypted message is: \n' + finalWord)

main()