#!/usr/bin/env python3

import sys, pprint

data = [ s.rstrip() for s in open(sys.argv[1]) ]

DX = { '^':0, 'v': 0, '<':-1, '>':1 }
DY = { '^':1, 'v':-1, '<': 0, '>':0 }

for line in data:
    x = y = 0;           pos = [ [0,0], [0,0] ]
    visited = { (x,y) }; visited2 = { (x,y) }
    for i, c in enumerate(line):
        x, y = x + DX[c], y + DY[c]
        visited.add(tuple([x,y]))

        pos[i%2] = [ pos[i%2][0] + DX[c], pos[i%2][1] + DY[c] ]
        visited2.add(tuple(pos[i%2]))

    print("Part 1:", len(visited))
    print("Part 2:", len(visited2))
