import sys

s, text = sys.stdin.read(1), ""
while s != "":
    if s.isalnum() == True:
        text += s.lower()
    else:
        text += " "
    s = sys.stdin.read(1)

i, d, text = 0, {}, text.split()
while i < len(text):
    if text[i].strip() not in d:
        d[text[i].strip()] = True
    i += 1

print(len(d))