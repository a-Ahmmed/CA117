import sys

s = sys.stdin.readline()
while s != "":
    s = s.split()
    if s[0].lower() in s[1].lower():
        print("True")
    else:
        print("False")
    s = sys.stdin.readline()