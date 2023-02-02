import sys

s = sys.stdin.readline()
while s != "":
    s = s.split()
    i = 0
    j = 0
    
    while i < len(s) and j == 0:
        if s[i][0] == "m":
            s[i] = s[i].capitalize()
            j = 1
        i += 1

    print(" ".join(s))

    s = sys.stdin.readline()