#!/usr/bin/env python3

import sys, pprint, collections, tqdm

grid = { complex(x, y): c for y, line in enumerate(open(sys.argv[1]))
                          for x, c in enumerate(line.strip()) }

start, = [a for a in grid if grid[a] == 'S']
end,   = [a for a in grid if grid[a] == 'E']

def bfs(grid):
    q, seen = collections.deque([(0, start)]), {start:0}
    while q:
        cost, pos = q.popleft()

        for d in (1, -1j, -1, 1j):
            npos = pos + d
            if npos in grid and grid[npos] != '#' and npos not in seen:
                seen[npos] = cost + 1
                q.append((cost + 1, npos))

    return seen

dist = lambda a,b: abs(a.real - b.real) + abs(a.imag - b.imag)

def shortcut(steps):
    res = collections.defaultdict(int)
    for pos in tqdm.tqdm(cost):
        for d in [ complex(x,y) for x in range(-steps,steps+1)
                                for y in range(-steps,steps+1)
                                   if 0 < dist(pos,pos+complex(x,y)) <= steps ]:
            npos = pos + d
            if npos in cost:
                save = cost[npos] - cost[pos] - dist(npos,pos)
                if save > 0: res[save] += 1
    return res

cost = bfs(grid)
print("Original distance:", cost[end])

for steps in (2,20):
    cheats = shortcut(steps)
    res = sum(cheats[k] for k in sorted(cheats) if k >= 100)
    print(f"Cheats that save >100ps for {steps} steps: {res}")
