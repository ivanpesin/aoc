#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    data = { (i,j): ch for i,s in enumerate(f) for j,ch in enumerate(s.strip()) }

res, more, p1 = [], True, True
while more:
    more = False
    for i,j in [ a for a in data if data[a] == '@' ]:
        n = sum(1 for di,dj in [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)] if data.get((i+di,j+dj),'.') == '@')
        if n < 4:
            res.append((i,j))
            more = True
    for i,j in res: data[i,j] = '.'
    if p1:
        print(f'Part 1: {len(res)}')
        p1 = False

print(f'Part 2: {len(res)}')