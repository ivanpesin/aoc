#!/usr/bin/env python3

import sys, string

with open(sys.argv[1]) as f:
    data = [ l.strip() for l in f ]

score = 0
for l in data:
    a, b = l[:len(l)//2], l[len(l)//2:]
    c, = set(a) & set(b)
    score += string.ascii_letters.index(c) + 1

print(f"Part 1: {score}")

score = 0
for i in range(0,len(data),3):
    c, = set(data[i]) & set(data[i+1]) & set(data[i+2])
    score += string.ascii_letters.index(c) + 1

print(f"Part 2: {score}")
