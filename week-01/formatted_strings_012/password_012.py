import sys

s = sys.stdin.readline()
while s != "":
    s, i, dc, lc, uc, sc = s.strip(), 0, 0, 0, 0, 0
    
    while i < len(s):
        if dc == 0 and s[i].isdigit() == True:
            dc += 1
        elif lc == 0 and s[i].islower() == True:
            lc += 1
        elif uc == 0 and s[i].isupper() == True:
            uc += 1
        elif dc == 0 and lc == 0 and uc == 0 and sc == 0:
            sc += 1
        i += 1
    
    print(dc + lc + uc + sc)
    s = sys.stdin.readline()