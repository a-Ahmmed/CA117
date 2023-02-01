import sys

s = sys.stdin.readline()
while s != "":
    s = int(s.strip()) + 1

    num = [n for n in range(11,s) if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0]
    print(f'Primes: {[2,3,5,7] + num}')

    s = sys.stdin.readline()