import sys

d = {"A":True, "B":True, "C":True, "D":True, "E":True, "F":True}
nums = sorted(sys.stdin.readline().split())
d = {key : nums[i] for i, key in enumerate(d)}
l = [d[c] for c in sys.stdin.readline().rstrip()]

print(" ".join(l))