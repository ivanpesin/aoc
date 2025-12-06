#!/usr/bin/env python3

from math import prod
import sys, pprint

data = [ s.strip().split() for s in open(sys.argv[1]).readlines() ]
op, res = { '+': sum, '*': prod }, 0

for i in range(len(data[0])):
    res += op[data[-1][i]]([ int(row[i]) for row in data[:-1] ])
print(f'Part 1: {res}')

data = { (x,y): ch for y,s in enumerate(open(sys.argv[1]).readlines())
                   for x,ch in enumerate(s.strip('\n')) }

max_x, max_y = max(x for x,y in data), max(y for x,y in data)

digits, nums, o, res = [], [], None, 0
for x in range(max_x, -1, -1):
    for y in range(max_y+1):
        if data.get((x,y), ' ').isdigit(): digits.append(data[x,y])
        elif data.get((x,y), ' ') in '+*': o = op[data[x,y]]
    if not digits: continue
    nums.append(int(''.join(digits))); digits = []
    if o is not None:
        res += o(nums)
        nums, o = [], None

print(f'Part 2: {res}')

