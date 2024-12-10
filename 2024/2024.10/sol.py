#!/usr/bin/env python3

import sys, pprint, collections

grid = { (x, y): cell for y, row  in enumerate(open(sys.argv[1]))
                      for x, cell in enumerate(row.strip())       }

trailheads = [ (x, y) for x, y in grid if grid[x, y] == '0' ]

def bfs(start, part2):
    queue = collections.deque([start])
    visited = [start]
    while queue:
        x, y = queue.popleft()
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if (x+dx, y+dy) in grid and \
                (part2 or (x+dx, y+dy) not in visited) and \
                int(grid[x+dx, y+dy]) - int(grid[x,y]) == 1:
                queue.append((x+dx, y+dy))
                visited.append((x+dx, y+dy))
    return visited

res1 = res2 = 0
for trailhead in trailheads:
    res1 += sum(1 for a in bfs(trailhead,part2=False) if grid[a] == '9')
    res2 += sum(1 for a in bfs(trailhead,part2=True) if grid[a] == '9')

print("Part 1:", res1)
print("Part 2:", res2)
