#!/usr/bin/env python3

import sys, pprint, heapq, collections

data = { (r,c): int(ch) for r,s in enumerate(open(sys.argv[1]).readlines())
                        for c,ch in enumerate(s.strip()) }
rows, cols = [ a+1 for a in max(data) ]

def dist(start, end, min_span, max_span):
    # cost, pos, dir, span, path
    heapq.heapify(todo := [ (0, start, (0,1), 0 ), (0, start, (1,0), 0 ) ])
    seen = {}
    while todo:
        # pprint.pp(todo)
        cost, pos, dir, span = heapq.heappop(todo)
        if pos == end and span >= min_span: return cost

        for d in sorted([dir, (dir[1],dir[0]), (-dir[1],-dir[0])], key=lambda x: data.get((pos[0]+x[0],pos[1]+x[1]), 0)):
            npos = (pos[0]+d[0], pos[1]+d[1])
            if npos not in data: continue
            if d != dir and span < min_span: continue
            if d == dir and span >= max_span: continue
            t = (npos, d, span+1 if d == dir else 1)
            if t in seen and seen[t] <= cost+data[npos]: continue
            heapq.heappush(todo, (cost+data[npos], *t))
            seen[t] = cost+data[npos]

print("Part 1:", dist((0,0), (rows-1,cols-1), 1, 3))
print("Part 2:", dist((0,0), (rows-1,cols-1), 4, 10))


