#!/usr/bin/env python3

import sys, pprint

with open(sys.argv[1]) as f: 
    data = [ l.strip() for l in f ]

DIR = { 'L': (-1,0), 'R': (1,0), 'U': (0,-1), 'D': (0,1) }

knots = int(sys.argv[2])
knot = [ [0,0] for _ in range(knots) ]
visited = set()
visited.add(tuple(knot[-1]))

for l in data:
    d, n = l.split()

    for _ in range(int(n)):
        knot[0] = [ sum(p) for p in zip(knot[0], DIR[d]) ]
        for k in range(1,knots):
            dist = [ abs(p[0]-p[1]) for p in zip(knot[k-1],knot[k]) ]
            if max(dist) > 1:
                dx = dy = 0
                if abs(knot[k-1][0] - knot[k][0]) > 0: dx = (knot[k-1][0] - knot[k][0]) / abs(knot[k-1][0] - knot[k][0])
                if abs(knot[k-1][1] - knot[k][1]) > 0: dy = (knot[k-1][1] - knot[k][1]) / abs(knot[k-1][1] - knot[k][1])
                knot[k][0] += dx
                knot[k][1] += dy
                if k == knots - 1: visited.add(tuple(knot[k]))

print(f"Answer with {knots} knots: {len(visited)}")
