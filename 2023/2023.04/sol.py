#!/usr/bin/env python3

import sys, pprint
import re, collections

data = [ s.strip() for s in open(sys.argv[1]).readlines() ]

p1, p2 = [], collections.defaultdict(int)
for n,s in enumerate(data):
    left, right = data[n].split(': ')[1].split(' | ')
    wins  = set([int(t) for t in left.split()])
    haves = set([int(t) for t in right.split()])
    cnt = len(wins & haves)
    if cnt > 0: p1.append(2**(cnt-1))
    for i in range(cnt): p2[n+i+1] += p2[n]+1

print(sum(p1))
print(sum(v+1 for v in p2.values()))