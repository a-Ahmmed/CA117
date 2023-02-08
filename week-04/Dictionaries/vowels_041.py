import sys

d = {
    "a" : 0,
    "e" : 0,
    "i" : 0,
    "o" : 0,
    "u" : 0,
}

s = sys.stdin.read(1)
while s != "":
    try:
        d[s.lower()] += 1
    except KeyError:
        pass
    s = sys.stdin.read(1)

def tagger(item):
    return item[1]

length = len(str(max(d.values())))
for k, v in sorted(d.items(), key=tagger, reverse=True):
    print(f'{k} : {v:>{length}}')