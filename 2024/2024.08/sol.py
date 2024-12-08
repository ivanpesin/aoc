#!/usr/bin/env python3

import sys, pprint, collections, itertools

grid = { (x, y): cell for y, row in enumerate(open(sys.argv[1]))
                      for x, cell in enumerate(row.strip())  }

freqs = collections.defaultdict(list)
for a in grid:
    if grid[a] != '.': freqs[grid[a]].append(a)

def solve(part2=False):
    nodes = set()
    for a in freqs:
        for one, two in itertools.combinations(freqs[a], 2):
            x1, y1, x2, y2 = *one, *two
            dx, dy = x2-x1, y2-y1
            if part2:
                nodes |= set([(x1, y1), (x2, y2)])
                while (x1 - dx, y1 - dy) in grid:
                    x1, y1 = x1 - dx, y1 - dy
                    nodes.add((x1, y1))
                while (x2 + dx, y2 + dy) in grid:
                    x2, y2 = x2 + dx, y2 + dy
                    nodes.add((x2, y2))
            else:
                if (x1 - dx, y1 - dy) in grid: nodes.add((x1 - dx, y1 - dy))
                if (x2 + dx, y2 + dy) in grid: nodes.add((x2 + dx, y2 + dy))

    return len(nodes)

print("Part 1:", solve())
print("Part 2:", solve(part2=True))
