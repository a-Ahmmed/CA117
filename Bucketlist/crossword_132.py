#!/usr/bin/env python3

import sys

def commonChar(str1, str2):
    chars = set(str1) & set(str2)
    index = 0

    for c in chars:
        tmp = str2.rfind(c)
        if tmp > index:
            index = tmp
    
    char = str2[index]
    return index, char

def gridOutput(char, index, length, str2, target):
    if char != target:
        return (("." * index) + char + ("." * (length - index - 1)))
    else:
        return str2

def main():
    words = sys.stdin.readline().split()
    index, target = commonChar(words[0], words[1])
    length = len(words[1])

    for c in words[0]:
        print(gridOutput(c, index, length, words[1], target))

if __name__ == "__main__":
    main()