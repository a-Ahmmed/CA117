import sys

a = sys.stdin.readlines()
maxlen = 0
i = 0

while i < len(a):
    if len(a[i]) > maxlen:
        maxlen = len(a[i])    
    i += 1

i = 0
while i < len(a):
    s = a[i].strip()
    padding = (maxlen - len(a[i])) // 2
    print((" " * padding) + s)
    i += 1