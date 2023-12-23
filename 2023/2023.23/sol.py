#!/usr/bin/env python3

import sys, graphlib, pprint
from functools import cache

sys.setrecursionlimit(100000)

data = { complex(c,r): ch for r, s in enumerate(open(sys.argv[1])) for c, ch in enumerate(s.strip()) }
rows, cols = max(c.imag for c in data)+1, max(c.real for c in data)+1

start = [ p for p in data if p.imag == 0      and data[p] == '.' ][0]
end   = [ p for p in data if p.imag == rows-1 and data[p] == '.' ][0]

print(start, end)

q, res = [(0,start, set( (start,) ))], []
while q:
    dist, p, seen = q.pop(0)
    seen = seen.copy()
    if p == end: res.append(dist); continue

    for d in [1j, -1j, 1, -1]:
        t = data.get(p+d)
        if t is None or t == '#': continue
        if   data.get(p) == '>' and d != 1: continue
        elif data.get(p) == '<' and d != -1: continue
        elif data.get(p) == '^' and d != -1j: continue
        elif data.get(p) == 'v' and d != 1j: continue

        if p+d not in seen: seen.add( p+d ); q.append( (dist+1,p+d, seen) );

# print(res)
print("Part 1:", max(res))

# compressing graph
todo = [ (0, start, start, start) ]
node_dist, adj = {}, { start: set() }
while todo:
    dist, p, prev_p, prev_node = todo.pop(0)

    ways, next = 0, []
    for d in [1j, -1j, 1, -1]:
        t = data.get(p+d)
        if t is None or t == '#' or p+d == prev_p: continue
        ways += 1; next.append(p+d)
    if ways > 1 or p == end:
        node_dist[(prev_node, p)] = node_dist[(p, prev_node)] = dist
        adj[prev_node].add(p);
        if p in adj:
            adj[p].add(prev_node)
            next = []
        else: adj[p] = set((prev_node,))
        prev_node, dist = p, 0
    for k in next:
        todo.append( (dist+1, k, p, prev_node) )

todo, res = [ (0, start, set()) ], 0
while todo:
    dist, p, visited = todo.pop()
    if p == end: res = max(res, dist)

    for k in adj[p]:
        if k not in visited: todo.append( (dist+node_dist[(p,k)],k, visited | set((k,))) )

print("Part 2:", res)