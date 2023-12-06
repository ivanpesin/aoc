#!/usr/bin/env python3

import sys, pprint, math, re

duration, dist = [], []
with open(sys.argv[1]) as f:
    duration = [ int(n) for n in re.findall(r'\d+', f.readline()) ]
    dist = [ int(n) for n in re.findall(r'\d+', f.readline()) ]

res = []
for n, maxtime in enumerate(duration):
    a = [ (maxtime - t)*t for t in range(maxtime+1) ]
    res.append(len([ i for i in a if i > dist[n] ]))

print("Solution:", math.prod(res))