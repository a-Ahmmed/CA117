import sys

s = sys.stdin.readline()
while s != "":
    s = s.strip()
    if len(s) % 2:
        print(s[len(s)//2])
    else:
        print("No middle character!")
    s = sys.stdin.readline()