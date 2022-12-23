def main():
    # leets compiled from https://www.gamehouse.com/blog/leet-speak-cheat-sheet/
    # single character leet
    singleChar = {
        "a": ["4", "@", "^"],
        "b": ["8", "6"],
        "c": ["[", "¢", "{", "<", "(", "©"],
        "d": [")", "?", ">"],
        "e": ["3", "&", "£", "€", "ë"],
        "f": ["ƒ", "v"],
        "g": ["&", "6", "9"],
        "h": ["#"],
        "i": ["1", "|", "!"],
        "j": ["]", ";", "1"],
        "k": [],
        "l": ["1", "£", "7", "|"],
        "m": [],
        "n": ["^"],
        "o": ["0", "Q", "p", "Ø"],
        "p": ["9", "?"],
        "q": ["0", "2", "&"],
        "r": ["2", "®"],
        "s": ["5", "$", "z", "§", "2"],
        "t": ["7", "+", "†"],
        "u": ["v", "µ"],
        "v": [],
        "w": [],
        "x": ["×", "?"],
        "y": ["j", "7", "¥"],
        "z": ["2", "s", "%"]
    }
    # double character leet
    doubleChar = {
        "a": ["(L"],
        "b": ["I3", "13", "|3", "!3", "(3", "/3", ")3", "j3"],
        "c": [],
        "d": ["|)", "(|", "[)", "I>", "|>", "T)", "I7", "cl", "|}", "|]"],
        "e": ["[-"],
        "f": ["|=", "|#", "ph", "/="],
        "g": ["C-", "[,", "{,", "<-", "(."],
        "h": ["}{"],
        "i": ["[]", "]["],
        "j": ["_|", "_]"],
        "k": [">|", "|<", "/<", "1<", "|c", "|(", "|{"],
        "l": ["|_"],
        "m": ["^^", "nn"],
        "n": ["^/", "|V", "/V"],
        "o": ["()", "oh", "[]", "<>"],
        "p": ["|*", "|o", "|º", "|^", "|>", "|°", ".-", "|2", "|-"],
        "q": ["0_", "<|"],
        "r": ["I2", "|`", "|~", "|?", "/2", "|^", "lz", "|9", "12", "[z", "|9"],
        "s": ["es"],
        "t": [],
        "u": ["L|"],
        "v": ["|/"],
        "w": ["VV", "uu", "2u", "v²"],
        "x": ["><", "}{", ")(", "]["],
        "y": ["`/"],
        "z": ["7_", ">_"]
    }

    f1 = open("test.txt", "r")
    f2 = open("out.txt", "w")

    for line in f1:
        line = line.strip("\n")
        for char1 in range(len(line)):
            for leet1 in singleChar[line[char1]]: # if character has leet replace it
                leetWord = line[:char1] + leet1 + line[char1 + 1:]
                for char2 in range(len(leetWord)): # do the same but for double character starting at index
                    if char2 != char1:
                        for leet2 in doubleChar[line[char2]]:
                            leetWord2 = leetWord[:char2] + leet2 + leetWord[char2 + 1:]
                            f2.write(leetWord2 + "\n")

main()