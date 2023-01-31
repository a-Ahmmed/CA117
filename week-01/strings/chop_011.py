import sys

s = sys.stdin.readline()
while s != "":
    s = s[1:len(s)-2]
    if s:
        print(s)
    s = sys.stdin.readline()