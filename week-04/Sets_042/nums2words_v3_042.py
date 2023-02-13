import sys

with open(sys.argv[1], "r") as f:
    tr = [line.split()[1] for line in f]

for s in sys.stdin:
    s = s.split()
    for i, digit in enumerate(s):
        s[i] = tr[int(digit)]
    print(" ".join(s))