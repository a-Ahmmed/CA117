import sys
import string

a, d = sys.stdin.read().split(), {}

for s in a:
    i, j = 0, 1
    while i < len(s) and j == 1:
        if s[i] not in string.punctuation or s[i] == "'":
            i += 1
        else:
            j = 0
    
    s = s[:i]

    if s.lower() not in d:
        d[s.lower()] = 1
    else:
        d[s.lower()] += 1

for k, v in sorted(d.items()):
    print(f'{k} : {v}')