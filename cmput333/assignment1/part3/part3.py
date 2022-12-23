def main():

    f = open("ciphertext3", "rb")
    f1 = open("ciphertext3.mod", "wb")
    gOnetoTen = f.read(16 * 10)
    f.seek(16 * 12)
    group13 = f.read(16)
    f.seek(16 * 11)
    rest = f.read()

    f1.write(gOnetoTen + group13 + rest)

main()