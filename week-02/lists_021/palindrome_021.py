import sys

s = sys.stdin.readline()
while s != "":
    s = s.strip().lower()

    i = 0
    while i < len(s):
        if s[i].isalnum() != True:
            s = s.replace(s[i], "")
        i += 1
    
    if s == s[::-1]:
        print("True")
    else:
        print("False")
    
    s = sys.stdin.readline()