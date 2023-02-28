#!/usr/bin/env python3

from perfect_062 import get_divisors, get_proper_divisors, is_perfect

def main():

    print(get_divisors(6))
    print(get_proper_divisors(6))
    print(is_perfect(6))

    numbers = [1, 2, 3, 4, 5, 6, 28, 496, 8128, 8129]

    for n in numbers:
        print(is_perfect(n))

if __name__ == '__main__':
    main()