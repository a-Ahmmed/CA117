#!/usr/bin/env python3

import sys

for line in sys.stdin:
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for c in line:
        alphabet = alphabet.replace(c.lower(), "")
    
    if len(alphabet) > 0:
        print(f'missing {alphabet}')
    else:
        print("pangram")