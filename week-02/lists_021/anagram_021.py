import sys

s = sys.stdin.readline()
while s != "":
    s = s.split()
    if sorted(s[0]) == sorted(s[1]):
        print("True")
    else:
        print("False")
    s = sys.stdin.readline()