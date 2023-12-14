#!/usr/bin/env python3

import sys, pprint, collections

platform = { (r,c): ch for r,s in enumerate(open(sys.argv[1]).readlines())
             for c,ch in enumerate(s.strip()) }
rows, cols = max(r for r,_ in platform) + 1, max(c for _,c in platform) + 1
D = ((-1,0), (0,-1), (1,0), (0,1)) # N W S E

def sink(r,c, direction):
    dr, dc = direction
    while 0 <= r+dr < rows and 0 <= c+dc < cols:
        if platform[r+dr,c+dc] != '.': break
        platform[r+dr,c+dc], platform[r,c] = 'O', '.'
        r,c = r+dr,c+dc

weight = lambda: sum(rows-r for r in range(rows) for c in range(cols) if platform[r,c] == 'O')

res = []
for i in range(int(sys.argv[2])):
    cycle = []
    for d in D:
        for r in range(rows):
            for c in range(cols):
                rr,cc = r,c
                if d in [(1,0), (0,1)]: rr,cc = rows-1-r, cols-1-c
                if platform[rr,cc] == 'O': sink(rr,cc, d)
        cycle.append(weight())

    if tuple(cycle) in res:
        cstart = res.index(tuple(cycle))
        clen = i - cstart
        print(f"Cycle found at iteration {i}, cstart {cstart}, clen {clen}")
        pos = (1_000_000_000 - cstart) % clen
        print(f"Part 2:", res[cstart+pos-1])
        break
    res.append(tuple(cycle))