import sys

with open(sys.argv[1], "r") as f:
    censors = [line.rstrip() for line in f]
a = [line.rstrip() for line in sys.stdin]

for censor in censors:
    i = 0
    while i < len(a):
        a[i] = a[i].replace(censor, "@" * len(censor))
        i += 1

for line in a:
    print(line)