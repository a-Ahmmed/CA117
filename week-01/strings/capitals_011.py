import sys

s = sys.stdin.readline()
while s != "":
    print(s[:len(s) - 2].capitalize() + s[-2].capitalize())
    s = sys.stdin.readline()