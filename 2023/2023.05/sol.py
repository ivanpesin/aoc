#!/usr/bin/env python3

import sys, pprint
import re, collections

seeds, maps = [], collections.defaultdict(list)
for s in open(sys.argv[1]).read().split('\n\n'):
    if 'seeds:' in s:
        seeds = [ int(n) for n in re.findall(r'\d+', s) ]
        continue

    t = s.split(' ')[0]
    for l in s.split('\n')[1:]:
        maps[t].append([ int(n) for n in re.findall(r'\d+', l) ])

res = []
for seed in seeds:
    dst = seed
    for t in maps:
        for m in maps[t]:
            if m[1] <= dst < m[1] + m[2]:
                dst = m[0] + (dst - m[1])
                break
    res.append(dst)

print("Part 1:", min(res))

res, rseeds = [], [ (n,n+r-1) for n,r in list(zip(seeds,seeds[1:]))[::2] ]

while rseeds:
    current, next = [], [ rseeds.pop(0) ]
    for t in maps:
        current, next = next[:], []
        while current:
            start, end = current.pop(0)
            matched = False
            for m in maps[t]:
                a,b, delta = m[1], m[1] + m[2] - 1, m[0] - m[1]
                if min(end,b) - max(start,a) >= 0:  # overlap
                    points = sorted([start,end,a,b])
                    if start < a: current.append(tuple([points[0], points[1]-1]))
                    if end > b:   current.append(tuple([points[2]+1, points[3]]))
                    start, end = points[1] + delta, points[2] + delta
                    next.append(tuple([start,end]))
                    matched = True
                    break
            if not matched: next.append(tuple([start,end]))

    res.append(min([ p[0] for p in next ]))

print("Part 2:", min(res))