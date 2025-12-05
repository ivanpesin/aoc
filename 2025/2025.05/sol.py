#!/usr/bin/env python3

import sys, pprint
from itertools import chain

data = open(sys.argv[1]).read()

i, ranges = 2, [*chain.from_iterable(sorted( tuple(int(n) for n in s.split('-')) for s in data.split('\n\n')[0].split('\n') ))]
while i < len(ranges):
    if ranges[i] <= ranges[i-1]:
        del ranges[i]
        if ranges[i] <= ranges[i-1]: del ranges[i]
        else: del ranges[i-1]
    else: i += 2

p1 = p2 = 0; first = True
for pid in data.split('\n\n')[1].split('\n'):
    for i in range(0, len(ranges), 2):
        a, b = ranges[i], ranges[i+1]
        if first: p2 += len(range(a, b+1))
        if int(pid) in range(a,b+1): p1 += 1
    first = False

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')