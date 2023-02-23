#!/usr/bin/env python3

import sys

for line in sys.stdin:
    squashed = []
    countChar = line[0]
    count = 0
    
    for char in line:
        if char == countChar:
            count += 1
        else:
            squashed.append(str(count) + countChar)
            countChar = char
            count = 1
   
    print("".join(squashed))
