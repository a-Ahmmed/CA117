import sys

s = sys.stdin.readline()
while s != "":
    s = int(s.strip()) + 1

    num = [n if n % 3 == 0 else 0 for n in range(1,s)]
    print(f'Non-multiples of 3 replaced: {num}')

    s = sys.stdin.readline()