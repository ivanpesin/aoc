#!/usr/bin/env python3

import sys, itertools

with open(sys.argv[1]) as f:
    data = [ list(map(int, r.split('-'))) for r in f.readline().strip('\n').split(',') ]

p1 = p2 = 0
for a, b in data:
    for i in range(a, b + 1):
        s, l = str(i), len(str(i))
        if s[:l//2] == s[l//2:]: p1 += i
        for j in range(l//2, 0, -1):
            if len(set(itertools.batched(s, j))) == 1:
                p2 += i
                break

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')