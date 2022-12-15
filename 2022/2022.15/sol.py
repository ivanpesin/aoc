#!/usr/bin/env python3

import sys, re, collections, pprint

with open(sys.argv[1]) as f:
    data = [ list(map(int,re.findall(r'-?\d+', l))) for l in f ]

dist = lambda p,q: (abs(p[0]-q[0]) + abs(p[1]-q[1]))
grid = collections.defaultdict(lambda: [])
    
for sx,sy,bx,by in data:
    d = dist((sx,sy),(bx,by))
    for i in range(d+1):
        ay1, ay2 = sy - i, sy + i
        ax1, ax2 = sx - d + i, sx + d - i
        grid[ay1].append([ax1,ax2])
        grid[ay2].append([ax1,ax2])

for y in grid:
    if len(grid[y]) < 2: continue
    merged = []
    for interval in sorted(grid[y]):
        if merged and interval[0]-1 <= merged[-1][1]: merged[-1][1] = max(merged[-1][1],interval[1])
        else: merged.append(interval)
    grid[y] = merged

row = int(sys.argv[2])
print(f"Part 1: y={row}, positions={grid[row][0][1] - grid[row][0][0]}")

for y in grid:
    if not 0 <= y <= 4_000_000: continue
    if len(grid[y]) < 2: continue
    for i in range(1,len(grid[y])):
        x = grid[y][i-1][1]+1
        if grid[y][i][0]-1 == x: print(f"Part 2: beacon={x},{y} freq={x*4_000_000+y}")