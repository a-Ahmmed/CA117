#!/usr/bin/env python3

import sys

def main():
    swapTable = {
        "A": ["", 2, 1, 3],
        "B": ["", 1, 3, 2],
        "C": ["", 3, 2, 1]
    }

    num, swapChars = int(sys.stdin.readline()), sys.stdin.readline().rstrip()

    for c in swapChars:
        num = swapTable[c][num]

    print(num)

if __name__ == "__main__":
    main()