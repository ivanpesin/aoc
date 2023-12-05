#!/usr/bin/env python3

import sys, pprint, datetime, multiprocessing
import re, collections

seeds, maps = [], collections.defaultdict(list)
for s in open(sys.argv[1]).read().split('\n\n'):
    if 'seeds:' in s:
        seeds = [ int(n) for n in re.findall(r'\d+', s) ]
        continue

    t = s.split(' ')[0]
    for l in s.split('\n')[1:]: maps[t].append([ int(n) for n in re.findall(r'\d+', l) ])

def solve(idx, seeds):
    res, timer = None, datetime.datetime.now()
    for i, dst in enumerate(seeds):
        if i % 10_000_000 == 0: print(f"{idx}: {i=} {datetime.datetime.now() - timer}")
        for t in maps:
            for m in maps[t]:
                if m[1] <= dst < m[1] + m[2]:
                    dst = m[0] + (dst - m[1])
                    break
        res = dst if res is None else min(res, dst)

    return res

if __name__ == '__main__':

    print("Part 1:", solve(0, seeds))

    rseeds = []
    for n,r in list(zip(seeds,seeds[1:]))[::2]:
        for a in range (0, r, 100_000_000):
            rseeds.append(range(n+a, n+a+min(100_000_000, r-a)))

    with multiprocessing.Pool() as p:
        res = p.starmap(solve, zip(range(len(rseeds)), rseeds))

    print("Part 2:", min(res))