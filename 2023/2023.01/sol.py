#!/usr/bin/env python3

import sys


data = [ s.strip() for s in open(sys.argv[1]).readlines() ]

# Part 1
nums = []
for s in data:
    a = [ c for c in s if c.isdigit() ]
    nums.append(int(f"{a[0]}{a[-1]}"))
print("Part 1:", sum(nums))

# Part 2
tdigits = [ "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" ]
nums = []
for s in data:
    a = set()
    for ts in tdigits:
        if ts in s:
            a.add(tuple([s.index(ts),  tdigits.index(ts)+1]))
            a.add(tuple([s.rindex(ts), tdigits.index(ts)+1]))
    for i, c in enumerate(s):
        if c.isdigit(): a.add(tuple([i, int(c)]))

    b = sorted(a)
    nums.append(int(f"{b[0][1]}{b[-1][1]}"))

print("Part 2:", sum(nums))