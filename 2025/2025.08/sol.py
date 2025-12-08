#!/usr/bin/env python3

import sys, math, collections as coll
from itertools import combinations, groupby

jboxes = [ tuple(map(int, s.split(','))) for s in open(sys.argv[1]).readlines() ]

dist = { tuple(sorted((a,b))): math.dist(a,b) for a, b in combinations(jboxes, 2) }
uf = { v: i for i, v in enumerate(jboxes) }

for i, (a,b) in enumerate(sorted(dist, key=lambda x: dist[x])):
    b_id = uf[b]
    for k in uf:
        if uf[k] == b_id: uf[k] = uf[a]
    if i + 1 == int(sys.argv[2]):
        print('Part 1:', math.prod( c[1] for c in coll.Counter(uf.values()).most_common(3) ))
    if len(set(uf.values())) == 1:
        print(f'Part 2: {a[0]*b[0]}')
        break
