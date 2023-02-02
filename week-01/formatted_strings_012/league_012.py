import sys

s, maxlen = sys.stdin.readlines(), 0

i = 0
while i < len(s):
    line, j = s[i].split() , 1

    while line[j].isdigit() != True:
        j += 1

    if len(" ".join(line[1:j])) > maxlen:
        maxlen = len(" ".join(line[1:j]))
    i += 1

print(f'POS {"CLUB":<{maxlen}}  P   W   D   L  GF  GA  GD PTS')

i = 0
while i < len(s):
    line, j = s[i].split(), 1

    while line[j].isdigit() != True:
        j += 1
    
    print(f'{line[0]:>3} {" ".join(line[1:j]):<{maxlen}} {line[j]:>2} {line[j + 1]:>3} {line[j + 2]:>3} {line[j + 3]:>3} {line[j + 4]:>3} {line[j + 5]:>3} {line[j + 6]:>3} {line[j + 7]:>3}')
    i += 1