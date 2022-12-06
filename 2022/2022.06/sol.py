#!/usr/bin/env python3

import sys, collections

with open(sys.argv[1]) as f: 
    data = [ l.strip() for l in f ]

for n,l in enumerate(data):
    for part,step in enumerate([4,14]):
        print(f"Part {part+1}:")
        for i in range(step,len(l)+1):
            k, = collections.Counter(l[i-step:i]).most_common(1)
            if k[1] == 1:
                print(f" line={n}, start={i}")
                break
