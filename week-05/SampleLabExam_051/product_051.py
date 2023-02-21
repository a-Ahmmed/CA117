#!/usr/bin/env python3

import sys

num = int(sys.stdin.readline())
while num > 9:
    num = str(num)
    digits, resultstore, = [int(c) for c in num if c != "0"], 1
    
    for d in digits:
        resultstore *= d
    
    num = resultstore

print(num)