#!/usr/bin/env python3

import sys

disqualified, table = [], {}

for line in sys.stdin:
    line = line.split()
    name, scores = " ".join(line[:-3]), line[-3:]

    try:
        total = sum([int(d) for d in scores])
        table[name] = total
    except ValueError:
        disqualified.append(name)

for t in sorted(table.items(), key=lambda x: x[1]):
    print(f'{t[0]}: {t[1]}')

if len(disqualified) > 0:
    sys.stdout.write("Disqualified: ")
    print(*disqualified, sep=", ")