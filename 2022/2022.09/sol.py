#!/usr/bin/env python3

import sys, pprint

with open(sys.argv[1]) as f: 
    data = [ l.strip() for l in f ]

DIR = { 'L': (-1,0), 'R': (1,0), 'U': (0,-1), 'D': (0,1) }
sign = lambda n: -1 if n < 0 else 1

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
                if knot[k-1][0] != knot[k][0]: knot[k][0] += sign(knot[k-1][0] - knot[k][0])
                if knot[k-1][1] != knot[k][1]: knot[k][1] += sign(knot[k-1][1] - knot[k][1])
                if k == knots - 1: visited.add(tuple(knot[k]))

print(f"Answer with {knots} knots: {len(visited)}")
