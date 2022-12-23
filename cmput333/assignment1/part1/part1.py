from operator import itemgetter
from math import gcd


def create_hex_dump(file):
    with open(file, "rb") as f:
        binary_file = f.read()
    output = "ciphertext1_hex.txt"
    with open(output, "w") as hexdump:
        for character in binary_file:
            hexdump.write("{:02x}".format(character) + "\n")
    return output

# Frequency analysis
def freq_analysis(key_length, cipher_hex):
    freq_list = []
    max_bytes = []
    counter = {}
    # https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-2.php
    for i in range(key_length):
        for byte in cipher_hex[i::key_length]:
            if byte in counter:
                counter[byte] += 1
            else:
                counter[byte] = 1
        # Martijn Pieters - https://stackoverflow.com/a/30964597/17835165
        counter = {k: v / total for total in (sum(counter.values()),) for k, v in counter.items()}
        freq_list.append(counter)
        counter = {}
        # Priyanka Chaudhary - https://stackoverflow.com/a/268285/17835165
        byte = max(freq_list[i].items(), key=itemgetter(1))[0]
        max_bytes.append(byte)
    return max_bytes

def get_key(hex_dump, table):
    cipher_hex = [line.rstrip("\n") for line in open(hex_dump)]
    length = len(cipher_hex)
    # Byte occurrence counter for each byte read
    # Coincidence counting with a list
    occurrence = []
    for i in range(1, length):
        occurrence.append(0)
        for j in range(length):
            if (i + j) < length:
                if cipher_hex[j] == cipher_hex[i + j]:
                    occurrence[i - 1] += 1
    # Peaks represent positions with high occurence of bytes
    # Biv - https://crypto.stackexchange.com/a/40067
    peak = max(occurrence)
    second_peak = sorted(set(occurrence))[-2]
    index = occurrence.index(peak)
    second_index = occurrence.index(second_peak)
    # Python is 0-indexed
    position_max = index + 1
    position_second = second_index + 1
    # Guess key length by determining GCD of peak positions
    # GCD is the distance between each peak
    key_length = gcd(position_max, position_second)
    print("Peak {} at index {}".format(peak, index))
    print("Second peak {} at index {}".format(second_peak, second_index))
    print("Key length is {}".format(key_length))
    key = process_key(key_length, cipher_hex, table)
    return key

def process_key(key_length, cipher_hex, table):
    # Printable ASCII characters according to TA hints
    printable_hex = ["{:02x}".format(i) for i in range(32, 128)]
    printable_hex.append("{:02x}".format(10))
    printable_hex.append("{:02x}".format(13))

    # http://millikeys.sourceforge.net/freqanalysis.html
    # https://en.wikipedia.org/wiki/Letter_frequency
    # 20 is the hex code for space (highest occurring ASCII character in English text)
    # Each byte will be mapped to space
    space_hex = "{:02x}".format(ord(" "))
    bytes_list = freq_analysis(key_length, cipher_hex)
    key = []
    for byte in bytes_list:
        # Aaron Hall - https://stackoverflow.com/a/37221971/17835165
        # Convert hex to int for indexing the table
        ch, cl = int(byte[0], 16), int(byte[1], 16)

        ph, pl = int(space_hex[0], 16), int(space_hex[1], 16)

        kh, kl = hex(table[ph].index(ch)), hex(table[pl].index(cl))

        k = kh[2:] + kl[2:]
        if k in printable_hex:
            key.append(k)
    if key:
        print("Key:", key)
    return key

def decrypt(key, file, table):
    with open(file, "rb") as file:
        binary_file = file.read()
    bytes_list = []
    key_length = len(key)
    key_idx = 0
    try:
        for char in binary_file:
            byte = "{:02x}".format(char)
            if key_idx >= key_length:
                key_idx = 0
            ch, cl = int(byte[0], 16), int(byte[1], 16)

            key_byte = key[key_idx]
            kh, kl = int(key_byte[0], 16), int(key_byte[1], 16)

            # dmap method from Assignment #1 Lab Slide 3
            # Stephen Fuhry - https://stackoverflow.com/a/903867/17835165
            column_ph = [row[kh] for row in table]
            column_pl = [row[kl] for row in table]

            ph, pl = hex(column_ph.index(ch)), hex(column_pl.index(cl))

            bytes_list.append(int(ph[2:] + pl[2:], 16))

            key_idx += 1

        output = bytearray(bytes_list)
        with open("plaintext1.txt", "wb") as plaintext:
            plaintext.write(output)
        key = "".join([chr(int(i, 16)) for i in key])
        with open("key1.txt", "w") as key_text:
            key_text.write(key)
        print('Key is "{}" in ASCII'.format(key))
    except:
        print("Key length is not {}".format(len(key)))
        print("{} is not valid".format(key))

if __name__ == "__main__":
             #  0    1    2    3    4    5    6    7    8    9    A    B    C    D    E    F
    table =  [[0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6], # 0
              [0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8], # 1
              [0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9], # 2
              [0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0], # 3
              [0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa], # 4
              [0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe], # 5
              [0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf], # 6
              [0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd], # 7
              [0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb], # 8
              [0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4], # 9
              [0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5], # A
              [0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7], # B
              [0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc], # C
              [0x3, 0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2], # D
              [0x1, 0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3], # E
              [0x0, 0x8, 0x9, 0xb, 0xa, 0xe, 0xf, 0xd, 0xc, 0x4, 0x5, 0x7, 0x6, 0x2, 0x3, 0x1]] # F
    file = "ciphertext1"
    hex_dump = create_hex_dump(file)
    key = get_key(hex_dump, table)
    decrypt(key, file, table)
