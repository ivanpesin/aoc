#!/usr/bin/env python3

import sys, pprint, collections, time

grid = { (r,c): ch for r,s in enumerate(open(sys.argv[1]))
                   for c, ch in enumerate(s.strip()) }
ROWS, COLS = max([ r for r,_ in grid ])+1, max([ c for _,c in grid ])+1
start = [ p for p in grid if grid[p] == 'S' ][0]

def adj(g: dict, r,c: int):
    res = []
    if g[r,c] in 'S-': res = [ (r,c-1), (r,c+1) ]
    if g[r,c] in 'S|': res = [ (r-1,c), (r+1,c) ]
    if g[r,c] in 'SJ': res = [ (r-1,c), (r,c-1) ]
    if g[r,c] in 'SL': res = [ (r-1,c), (r,c+1) ]
    if g[r,c] in 'S7': res = [ (r+1,c), (r,c-1) ]
    if g[r,c] in 'SF': res = [ (r+1,c), (r,c+1) ]
    res = [ a for a in res if (0 <= a[0] < ROWS and 0 <= a[1] < COLS)]
    res = [ a for a in res if g[a] in '-|JL7F' ]
    return res

def maxdist(st: tuple):
    maxdist, loop = 0, collections.defaultdict(lambda: '.')
    q, seen = collections.deque([ (0, st) ]), set([ st ])
    while q:
        dist, (r,c) = q.popleft()
        maxdist = max(dist, maxdist)
        loop[r,c] = grid[r,c]
        for nr, nc in adj(grid, r,c):
            if (nr,nc) not in seen:
                q.append((dist + 1, (nr, nc)))
                seen.add((nr,nc))
    return maxdist, loop

res, pruned = maxdist(start)  # pruned grid contains only the loop chars, all garbage is filtered out
print("Part 1:", res)

def fill(st: tuple):
    queue, marked = collections.deque([ st ]), set([ st ])
    while queue:
        r, c = queue.popleft()
        for nr, nc in [ (r-1,c), (r+1,c), (r,c-1), (r,c+1) ]:
            if not (0 <= nr < ROWS and 0 <= nc < COLS): continue
            if pruned[nr,nc] != '.': continue
            if (nr,nc) not in marked:
                queue.append((nr, nc))
                marked.add((nr,nc))
        pruned[r,c] = 'O'

def walk(st, stick_side: tuple):
    stack, visited = [ st ], set()
    sr, sc = stick_side
    while stack:
        r,c = stack.pop()
        visited.add((r,c))

        if pruned[r+sr,c+sc] == '.': fill((r+sr,c+sc))
        if pruned[r,c] in '7L': sr, sc = -sc, -sr
        if pruned[r,c] in 'JF': sr, sc = sc, sr
        if pruned[r+sr,c+sc] == '.': fill((r+sr,c+sc))

        for nr, nc in adj(pruned, r,c):
            if (nr,nc) not in visited: stack.append((nr, nc))
        pruned[r,c] = 'x'

walk(start, tuple([*map(int,sys.argv[2:])]))

for r in range(ROWS): print(''.join([ pruned[r,c] for c in range(COLS) ]))

print("Part 2:", sum([ 1 for p in pruned if pruned[p] == '.' ]))
