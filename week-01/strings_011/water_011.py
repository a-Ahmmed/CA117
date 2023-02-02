import sys

water = int(sys.stdin.readline().strip())
buckets = sys.stdin.readline().split()
i = 0
j = 0

while i < len(buckets) and j == 0:
    water -= int(buckets[i])
    if water >= 0:
        i += 1
    else:
        j = 1

print(i)