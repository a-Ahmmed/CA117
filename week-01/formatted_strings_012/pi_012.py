import sys
import math

s = sys.stdin.readline()
while s != "":
    s = int(s.strip())
    print(f'{math.pi:.{s}f}')
    s = sys.stdin.readline()