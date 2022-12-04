#!/usr/bin/env python3

import sys, re

with open(sys.argv[1]) as f:
    data = [ [ int(b) for b in re.findall(r'\d+',l) ] for l in f ]

p1 = p2 = 0
for a,b,x,y in data:
    if (a >= x and b <= y) or (x >= a and y <= b): p1 += 1
    if (a <= x <= b) or (x <= a <= y):             p2 += 1

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")