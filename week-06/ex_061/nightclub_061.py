#!/usr/bin/env python3

import sys

maxCap = int(sys.stdin.readline())
Denied = 0
for line in sys.stdin:
    line = line.split()
    EorL = line[0]
    groupNum = int(line[1])

    if EorL == "enter":
        if groupNum < maxCap:
            maxCap -= groupNum
        else:
            Denied += 1
    else:
        maxCap += groupNum

print(Denied) 
