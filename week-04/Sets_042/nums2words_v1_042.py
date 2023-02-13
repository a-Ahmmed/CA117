import sys

words = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]

for line in sys.stdin:
    line = line.split()
    for i, c in enumerate(line):
        line[i] = words[int(c)]
    print(" ".join(line))