#!/usr/bin/env python3

import sys, re
from pprint import pp

with open(sys.argv[1]) as f:
    data = [ re.findall(r'([LR])(\d+)', s.rstrip('\n'))[0] for s in f ]

dial, ptr = 100, 50
p1 = p2 = 0

for turn, dist in data:
    print(f'Dial is rotated {turn}{dist}')
    if turn == 'L': delta = (ptr - int(dist))
    else: delta = (ptr + int(dist))

    print(f'   dial crosses `0` {abs(delta // dial)} times')
    p2 += abs(delta // dial)
    ptr = delta % dial

    print(f'   dial points to `{ptr}`')
    if ptr == 0: p1 += 1

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')