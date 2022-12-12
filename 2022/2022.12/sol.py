#!/usr/bin/env python3

import sys, collections

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

queue, seen, distto = collections.deque(), set(), {}

for p in [ pos ] if part == 2 else [ p for p in grid if grid[p] == "a" ]:
    queue.append(p)
    seen.add(p)
    distto[p] = 0

while queue:
    r,c = queue.popleft()
    if (r,c) == dest:
        print(f"Dist = {distto[r,c]}, {(r,c)}")
        break

    for nr,nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
        if (nr < 0 or nc < 0 or nr > height or nc > width): continue
        if ord(grid[nr,nc])-ord(grid[r,c]) > 1: continue
        if (nr,nc) not in seen: 
            queue.append((nr,nc))
            distto[nr,nc] = distto[r,c] + 1
            seen.add((nr,nc))