#!/usr/bin/env python3

import sys

for line in sys.stdin:
    nums = line.split()
    sNums = set(nums)

    uniqueNums = [int(d) for d in sNums if nums.count(d) == 1]
    try:
        print(max(uniqueNums))
    except ValueError:
        print("none")