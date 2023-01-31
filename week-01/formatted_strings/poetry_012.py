import sys

a, maxlen = sys.stdin.readlines(), 0

i = 0
while i < len(a):
    if len(a[i]) > maxlen:
        maxlen = len(a[i])    
    i += 1

i = 0
while i < len(a):
    s = a[i].strip()
    print(f"{s:^{maxlen - 1}}")
    i += 1