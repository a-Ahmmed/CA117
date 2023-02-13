import sys

words = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
d = {str(i) : words[i] for i in range(0,11)}

for line in sys.stdin:
    line = line.split()
    for i, c in enumerate(line):
        try:
            line[i] = d[c]
        except KeyError:
            line[i] = "unknown"
    print(" ".join(line))