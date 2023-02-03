import sys

with open(sys.argv[1], "r") as f:
    censors = [line.rstrip() for line in f]
a = [line.rstrip() for line in sys.stdin]

for censor in censors:
    for i, word in enumerate(a):
        a[i] = word.replace(censor, "@" * len(censor))

for line in a:
    print(line)