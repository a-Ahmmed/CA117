#!/usr/bin/env python3

import sys

animalLines = [set(line.split()) for line in sys.stdin.readlines()]
onEveryList = set()

for Aniset in animalLines:
    for animal in Aniset:
        if all([animal in s for s in animalLines]):
            onEveryList.add(animal)

print(len(onEveryList))

for animal in sorted(onEveryList):
    print(animal)
