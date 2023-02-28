#!/usr/bin/env python3

import sys

def get_divisors(n):
    dList = [d for d in range(1, n + 1) if n % d == 0]
    return dList

def get_proper_divisors(n):
    pdList = get_divisors(n)[:-1]
    return pdList

def is_perfect(n):
    return (sum(get_proper_divisors(n)) == n)