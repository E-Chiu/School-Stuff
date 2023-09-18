# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

encrypted = 'bA?B!4J8E14FF4DF7z.2A?B!82zF43'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?'

# capitalize the string in message
encrypted = encrypted.upper()

# run the encryption/decryption code on each symbol in the message string
for key in range(54):
    translated = ''
    for symbol in encrypted:
        if symbol in LETTERS:
            # get the encrypted (or decrypted) number for this symbol
            num = LETTERS.find(symbol) # get the number of the symbol
            num = num - key

            # handle the wrap-around if num is larger than the length of
            # LETTERS or less than 0
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            # add encrypted/decrypted number's symbol at the end of translated
            translated = translated + LETTERS[num]

        else:
            # just add the symbol without encrypting/decrypting
            translated = translated + symbol
    print('key: ' + LETTERS[key])
    print('message:' + translated)
    print('\n')

