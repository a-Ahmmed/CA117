import sys

d = {
    "A": 0,
    "B": 0,
    "C": 0,
}

num, abc, i = sys.stdin.readline().split(), sys.stdin.readline(), 0

while i < 3:
    num[i] = int(num[i])
    i += 1

d["A"], d["C"] = min(num), max(num)
num.remove(min(num))
num.remove(max(num))
d["B"] = num[0]

i, result = 0, []
while i < 3:
    result.append(str(d[abc[i]]))
    i += 1

print(" ".join(result))