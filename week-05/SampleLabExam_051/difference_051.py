#!/usr/bin/env python3

import sys

strs = [s.rstrip() for s in sys.stdin]
print(f'{strs[0]}\n{strs[1]}')

for i, c in enumerate(strs[0]):
    if strs[0][i] == strs[1][i]:
        sys.stdout.write("-")
    else:
        sys.stdout.write("*")
sys.stdout.write("\n")