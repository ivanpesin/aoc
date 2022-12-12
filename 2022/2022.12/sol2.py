#!/usr/bin/env python3

import sys
from collections import deque

grid, r = {}, 0
pos, dest = [], []
height = width = 0
part = int(sys.argv[2])

with open(sys.argv[1]) as f: 
    for l in f:
        for c in range(len(l.strip())): 
            grid[r,c] = l[c]
            if l[c] == 'S': pos,  grid[r,c] = tuple([r,c]), 'a'
            if l[c] == 'E': dest, grid[r,c] = tuple([r,c]), 'z'
        if r > height: height = r
        if c > width : width = c
        r += 1

fifo, seen, distto, edgeto = deque(), set(), {}, {}
if part == 1: 
    fifo.append(pos)
    seen.add(pos)
    distto[pos] = 0
else:    
    for p in grid:
        if grid[p] == "a":
            fifo.append(p)
            seen.add(p)
            distto[p] = 0

while fifo:
    r,c = fifo.popleft()
    if (r,c) == dest:
        print(f"Dist = {distto[r,c]}, {(r,c)}")
        break

    for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
        if nr < 0 or nc < 0: continue
        if nr > height or nc > width: continue
        if ord(grid[nr,nc])-ord(grid[r,c]) > 1: continue
        if (nr,nc) not in seen: 
            fifo.append((nr,nc))
            distto[nr,nc] = distto[r,c] + 1
            edgeto[nr,nc] = (r,c)
            seen.add((nr,nc))
