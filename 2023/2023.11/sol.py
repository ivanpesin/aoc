#!/usr/bin/env python3

import sys, pprint, itertools, time

grid = [ list(s.strip()) for s in open(sys.argv[1]) ]

expand_rows = [ r for r,l in enumerate(grid) if all(ch == '.' for ch in l) ]
expand_cols = [ c for c in range(len(grid[0])) if all(l[c] == '.' for l in grid) ]
star_positions = [ (r,c) for r,l in enumerate(grid) for c,v in enumerate(l) if v == '#' ]
pairs = list(itertools.combinations(star_positions, 2))

def dist(a,b, space_multiplier):
    row_range = range(a[0], b[0]+1) if a[0] < b[0] else range(b[0], a[0]+1)
    col_range = range(a[1], b[1]+1) if a[1] < b[1] else range(b[1], a[1]+1)

    return ( abs(a[0]-b[0]) + abs(a[1]-b[1]) +
             (sum([ r in row_range for r in expand_rows ]) +
              sum([ c in col_range for c in expand_cols ])) * (space_multiplier-1) )

print("Part 1:", sum([ dist(a,b,2) for a,b in pairs ]))
print("Part 2:", sum([ dist(a,b,10) for a,b in pairs ]))