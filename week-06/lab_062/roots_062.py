#!/usr/bin/env python3

import sys

def quadratic(a, b, c):
    discriminant = (b*b - 4*a*c) ** 0.5
    roots = [d/(2*a) for d in [-b + discriminant, -b - discriminant]]

    return roots

def imagCheck(roots):
    if str(roots[0])[-1] != ")":
        roots = sorted(roots)
        return (f'{roots[0]:.1f}, {roots[1]:.1f}')
    else:
        return None


for line in sys.stdin:
    abc = [int(d) for d in line.split()]
    roots = quadratic(abc[0],abc[1],abc[2])

    print(imagCheck(roots))