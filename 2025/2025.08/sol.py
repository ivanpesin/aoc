#!/usr/bin/env python3

import sys, math
from itertools import combinations, groupby

jboxes = [ tuple(map(int, s.split(','))) for s in open(sys.argv[1]).readlines() ]

distsq = lambda a,b: (a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2
dist = { distsq(a,b): sorted((a,b)) for a, b in combinations(jboxes, 2) }
uf = { v: i for i, v in enumerate(jboxes) }

cnt = 0
for k, v in sorted(dist.items()):
    a, b = v
    bid = uf[b]
    for k in uf:
        if uf[k] == bid: uf[k] = uf[a]
    cnt += 1
    if cnt == int(sys.argv[2]):
        print('Part 1:', math.prod( sorted([len(list(k)) for _,k in groupby(sorted(uf.values()))])[-3:] ) )
    if len(set(uf.values())) == 1:
        print(f'Part 2: {a[0]*b[0]}')
        break
