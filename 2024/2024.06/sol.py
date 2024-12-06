#!/usr/bin/env python3

import sys, pprint

grid = { (x, y): cell for y, row in enumerate(open(sys.argv[1]))
                      for x, cell in enumerate(row.strip())  }

max_x, max_y = max([ x for x, y in grid ]), max([ y for x, y in grid ])
start_x, start_y = [ a for a in grid if grid[a] == '^' ][0]
D = { 'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0) }

def has_loop(grid, part2=False):
    x,y, dir = start_x, start_y, 'N'
    visited, headings = { (x,y): 1 }, { (x,y): set([dir]) }
    p2_res = set()
    try:
        while True:
            dx, dy = D[dir]
            if grid[x+dx, y+dy] == '#':
                dir = { 'N':'E', 'E':'S', 'S':'W', 'W':'N' }[dir]
            else:
                x, y = x+dx, y+dy
                if part2 and (x,y) not in p2_res:
                    grid[x,y] = '#'
                    if has_loop(grid)[0]: p2_res.add((x,y))
                    grid[x,y] = '.'

                if (x,y) in visited:

                    if (dir in headings[x,y]): # we have a loop
                        return (True, len(visited.keys()))

                    visited[x,y] += 1
                    headings[x,y].add(dir)
                else:
                    visited[x,y] = 1
                    headings[x,y] = set([dir])

    except: pass
    if part2:   return False, len(p2_res)
    else:       return False, len(visited)

print("Part 1:", has_loop(grid, part2=False)[1])
print("Part 2:", has_loop(grid, part2=True)[1])