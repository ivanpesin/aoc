#!/usr/bin/env python3

import sys
from itertools import product

grid = {}
with open(sys.argv[1]) as f:
    for s in f: grid[tuple(map(int,s.split(',')))] = 6

cmin, cmax = list(grid)[0], list(grid)[0]
for x,y,z in grid:
    for dx,dy,dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        if (x+dx,y+dy,z+dz) in grid: grid[x,y,z] -= 1
    cmin, cmax = [ min(p) for p in zip(cmin,(x,y,z)) ], [ max(p) for p in zip(cmax,(x,y,z)) ]

print("Part 1:", sum(grid.values()))

cmin, cmax = [ v-1 for v in cmin ], [ v+1 for v in cmax ]
stack = [ tuple(cmin) ]
seen, area = set(stack[0]), 0
while stack:
    x,y,z = stack.pop(0)
    for dx,dy,dz in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]:
        v = (x+dx,y+dy,z+dz)
        if not all(cmin[i] <= v[i] <= cmax[i] for i in range(3)): continue
        if v in grid: area += 1
        else: 
            if v not in seen: 
                stack.append(v)
                seen.add(v)

print("Part 2:", area)