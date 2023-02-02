import sys

s = sys.stdin.readline()
while s != "":
    s = int(s.strip())

    mof3 = [n for n in range(1,s + 1) if n % 3 == 0]
    mof3sq = [n * n for n in mof3]
    mof4d = [n * 2 for n in range(1,s + 1) if n % 4 == 0]
    mofb = [n for n in range(1,s + 1) if n % 3 == 0 or n % 4 == 0]
    mofb2 = [n for n in mofb if n % 3 == 0 and n % 4 == 0]

    print(f'Multiples of 3: {mof3}')
    print(f'Multiples of 3 squared: {mof3sq}')
    print(f'Multiples of 4 doubled: {mof4d}')
    print(f'Multiples of 3 or 4: {mofb}')
    print(f'Multiples of 3 and 4: {mofb2}')

    s = sys.stdin.readline()