#!/usr/bin/env python3

import sys

for line in sys.stdin:
    greetingEs = line.rstrip()[1:-1]
    eStr= "e" * (len(greetingEs) * 2)
    print("h" + eStr + "y")
