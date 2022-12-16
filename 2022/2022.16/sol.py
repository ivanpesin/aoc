#!/usr/bin/env python3

import sys, functools

adj, rate = {}, {}
with open(sys.argv[1]) as f:
    for l in f:
        a, b = l.strip().split(';')
        _, v, _, _, r  = a.split()
        rate[v] = int(r.split('=')[1])
        adj[v] = b.replace(",","").split()[4:]

@functools.lru_cache(maxsize=None)
def maxflow(v, opened, time, part):
    if time < 1: 
        if part == 1: return 0
        else: return maxflow("AA", opened, 26, 1)
    best = 0

    for w in adj[v]:
        best = max(best, maxflow(w, opened, time - 1, part))

    if v not in opened:
        flow = rate[v] * (time - 1)
        open_more = opened | set([v])
        for w in adj[v]:
            if flow != 0: best = max(best, flow + maxflow(w, open_more, time - 2, part))

    return best

print("Part 1:", maxflow("AA", frozenset(), 30, 1))
print("Part 2:", maxflow("AA", frozenset(), 26, 2))
