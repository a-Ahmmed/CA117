import sys

s = sys.stdin.readline()
while s != "":
    s = s.split()
    s1 = "".join(sorted(s[0].lower()))
    s2 = "".join(sorted(s[1].lower()))

    if s1 in s2:
        print("True")
    else:
        print("False")
    
    s = sys.stdin.readline()