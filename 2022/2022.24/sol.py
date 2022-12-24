#!/usr/bin/env python3

import sys
from collections import deque
from functools import lru_cache

with open(sys.argv[1]) as f:
    data = [ s.strip() for s in f ]
    H, W = len(data), len(data[0])
    blizzards = { (r,c): s[c] for r,s in enumerate(data) for c in range(W) if s[c] not in ('.','#') }

FACE = { '>':(0,1), '<':(0,-1), '^':(-1,0), 'v':(1,0) }

@lru_cache(maxsize=None)
def mazeat(s):
    for step in range(s+1):
        nblizzards = {}
        for b,f in blizzards.items():
            r,c = b
            dr,dc = tuple(c * step for c in FACE[f])
            nr,nc = (r-1+dr)%(H-2)+1,(c-1+dc)%(W-2)+1
            if (nr,nc) in nblizzards: nblizzards[nr,nc].append(f)
            else: nblizzards[nr,nc] = [f]
    return nblizzards

def bfs(st,end,d):
    todo = deque([( *st, d )])
    seen = set(todo)
    while todo:
        r,c,d = todo.popleft()
        if (r,c) == end: return d

        nb = mazeat(d+1)
        for dr,dc in [(0,0),(-1,0),(1,0),(0,-1),(0,1)]:
            nr,nc = r+dr,c+dc
            if not ((0 < nr < H-1 and 0 < nc < W-1) or
                    (nr,nc) in [st, end]): continue
            if (nr,nc) in nb or (nr,nc,d+1) in seen: continue
            todo.append((nr,nc,d+1)); seen.add((nr,nc,d+1))

t = bfs((0,1),(H-1,W-2),0); print("There           :", t)
t = bfs((H-1,W-2),(0,1),t); print("And back        :", t)
t = bfs((0,1),(H-1,W-2),t); print("And there again :", t)