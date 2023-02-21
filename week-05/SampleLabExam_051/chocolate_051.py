#!/usr/bin/env python3

import sys

for line in sys.stdin:
    try:
        c = int(line.rstrip())

        if c % 400:
            print((c // 400) + 1)
        else:
            print(c // 400)
    except ValueError:
        print("Integer must be provided. Skipping...")