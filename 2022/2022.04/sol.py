#!/usr/bin/env python3

import sys, re

with open(sys.argv[1]) as f:
    data = [ [ int(b) for b in re.findall(r'\d+',l) ] for l in f ]

score = 0
for a,b,x,y in data:
    if (a >= x and b <= y) or \
       (x >= a and y <= b):
        score += 1

print(f"Part 1: {score}")

score = 0
for a,b,x,y in data:
    if (a <= x <= b) or \
       (x <= a <= y):
        score += 1

print(f"Part 2: {score}")
