#!/usr/bin/env python3

import sys, collections, heapq
import pprint, time

grid = { complex(x, y): c for y, line in enumerate(open(sys.argv[1]))
                          for x, c in enumerate(line.strip()) }

start, = [a for a in grid if grid[a] == 'S']
end,   = [a for a in grid if grid[a] == 'E']
SZ = int(max([ a.real for a in grid ]))

def draw(cost):
    print("\033[2J\033[H", end='', flush=True)
    for y in range(SZ+1):
        for x in range(SZ+1):
            p = complex(x, y)
            print('x' if p in cost else grid[p], end='')
        print()

def dijkstra(start, dir=1):
    queue = [(0, 0, start, dir)]
    cost, cnt = {start: 0}, collections.defaultdict(int)
    while queue:
        _, _, pos, dir = heapq.heappop(queue)

        # draw(cost)
        # print(cost[pos], pos)
        # time.sleep(0.1)

        for d in (1, -1j, -1, 1j):
            npos = pos + d
            if npos in grid and grid[npos] != '#' and npos not in cost:
                if dir == d: cost[npos] = cost[pos] + 1
                else:        cost[npos] = cost[pos] + 1001
                cnt[cost[npos]] += 1
                heapq.heappush(queue, (cost[npos], cnt[cost[npos]], npos, d))

    return cost

best_cost = dijkstra(start)[end]
print("Part 1:", best_cost)

def bfs(start):
    queue, seen, res = [(0, start, 1)], set(), set([start])
    while queue:
        cost, pos, dir = queue.pop(0)

        for d in (1, -1j, -1, 1j):
            if d == -dir: continue
            npos = pos + d
            if npos in grid and grid[npos] != '#' and (npos,cost) not in seen:
                est = dijkstra(npos, d)[end]
                if dir == d: cstep = 1
                else:        cstep = 1001
                if cost + cstep + est <= best_cost:
                    print(len(res), end='\r')
                    res.add(npos)
                    seen.add((npos,cost))
                    queue.append((cost + cstep, npos, d))

    return res

print("Part 2:", len(bfs(start)))