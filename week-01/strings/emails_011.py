import sys

s = sys.stdin.readline()
while s != "":
    i = 0
    while s[i].isdigit() != True:
        i += 1

    s = s[:i].split(".")
    print(s[0].capitalize(), s[1].capitalize())

    s = sys.stdin.readline()