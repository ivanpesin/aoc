import sys, collections
import pprint

grid, cutoff = {}, int(sys.argv[2])
for s in open(sys.argv[1]).readlines()[:cutoff]:
    x, y = [ int(a) for a in s.strip().split(',') ]
    grid[complex(x, y)] = '#'

maxx = max([int(a.real) for a in grid])
maxy = max([int(a.imag) for a in grid])

for y in range(maxy+1):
    for x in range(maxx+1):
        if complex(x, y) not in grid: grid[complex(x, y)] = '.'

def bfs(start, end):
    q, seen, step = collections.deque([(start,0)]), set(), 0
    while q:
        pos, step = q.popleft()
        if pos == end: return step
        for dir in [1, -1, 1j, -1j]:
            npos = pos + dir
            if npos in grid and grid[npos] != '#' and npos not in seen:
                q.append((npos, step+1))
                seen.add(npos)

print("Part 1:", bfs(0, complex(maxx, maxy)))

for n,s in enumerate(open(sys.argv[1]).readlines()[cutoff:]):
    x, y = [ int(a) for a in s.strip().split(',') ]
    grid[complex(x, y)] = '#'

    r = bfs(0, complex(maxx, maxy))
    if r is None:
        print(f"Part 2: {n+cutoff+1} @ {x},{y}")
        break
