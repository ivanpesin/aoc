#!/usr/bin/env python3

import sys, pprint, collections

grid = { x + y*1j: cell for y, row  in enumerate(open(sys.argv[1]))
                        for x, cell in enumerate(row.strip()) }

def bfs(start):
    plant = grid[start]
    queue, visited = collections.deque([start]), set([start])
    while queue:
        pos = queue.popleft()
        for step in (1, 1j, -1, -1j):
            if pos+step in grid and \
               pos+step not in visited \
               and grid[pos+step] == plant:
                queue.append(pos+step)
                visited.add(pos+step)
    return visited

plots, inspected = [], set()
for a in grid:
    if a in inspected: continue
    plot = bfs(a)
    inspected |= plot
    plots.append(plot)

perimeter = lambda plot: sum(1 for a in plot for step in (1, 1j, -1, -1j) if a + step not in plot)

def corners(plot):
    res = 0
    for a in plot:
        for d1,d2 in ((1, 1j), (1, -1j), (-1, 1j), (-1, -1j)):
            if a + d1 not in plot and a + d2 not in plot: res += 1
            if a + d1 in plot and a + d2 in plot and a + d1 + d2 not in plot: res += 1
    return res

res1 = res2 = 0
for p in plots:
    res1 += len(p) * perimeter(p)
    res2 += len(p) * corners(p)

print("Part 1:", res1)
print("Part 2:", res2)