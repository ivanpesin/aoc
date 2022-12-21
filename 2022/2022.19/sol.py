#!/usr/bin/env python3

import sys, re, collections, functools, multiprocessing

with open(sys.argv[1]) as f:
    blueprints = [ list(map(int,re.findall(r'\d+',s))) for s in f ]

def prune(bp, state):
    res = state[:]
    ore_max = max(bp[i] for i in (1,2,3,5))
    if res[5] > ore_max: res[5]=ore_max
    if res[6] > bp[4]:   res[6]=bp[4]
    if res[7] > bp[6]:   res[7]=bp[6]

    if res[1] >= res[-1]*ore_max-res[5]*(res[-1]-1):
        res[1] = res[-1]*ore_max-res[5]*(res[-1]-1)
    if res[2] >= res[-1]*bp[4]-res[6]*(res[-1]-1):
        res[2] = res[-1]*bp[4]-res[6]*(res[-1]-1)
    if res[3] >= res[-1]*bp[6]-res[7]*(res[-1]-1):
        res[3] = res[-1]*bp[6]-res[7]*(res[-1]-1)
    return res

def bfs(bp, timer):
    #            blueprint costs
    # bp:    nr, ore, clay, ore, clay, ore, obs
    # state: nr, ore, clay, obs, geo,  ore, clay, obs, geo, timer
    #           |resource counts      |robot counts        |
    best, state = 0, (-1, 0,0,0,0, 1,0,0,0, timer)
    todo = collections.deque([state])
    seen = { state }
    while todo:
        state = list(todo.popleft())
        best = max(best,state[4])
        if state[-1] == 0: continue

        state = prune(bp, state)

        nstates = []
        nstates.append(tuple([-1, *(sum(p) for p in zip(state[1:5], state[5:9])), *state[5:9], state[-1] - 1]))

        if state[1] >= bp[1]:
            nstate = list(nstates[0])
            nstate[1] -= bp[1]; nstate[5] += 1
            nstates.append(tuple(nstate))

        if state[1] >= bp[2]:
            nstate = list(nstates[0])
            nstate[1] -= bp[2]; nstate[6] += 1
            nstates.append(tuple(nstate))

        if state[1] >= bp[3] and state[2] >= bp[4]:
            nstate = list(nstates[0])
            nstate[1] -= bp[3]; nstate[2] -= bp[4]; nstate[7] += 1
            nstates.append(tuple(nstate))

        if state[1] >= bp[5] and state[3] >= bp[6]:
            nstate = list(nstates[0])
            nstate[1] -= bp[5]; nstate[3] -= bp[6]; nstate[8] += 1
            nstates.append(tuple(nstate))

        for nstate in nstates:
            if nstate not in seen:
                todo.append(nstate)
                seen.add(nstate)

    return best


with multiprocessing.Pool() as p:
    res = p.starmap(bfs, [ (b,24) for b in blueprints ])
print("Part 1:", sum((i+1)*n for i,n in enumerate(res)))

with multiprocessing.Pool() as p:
    res = p.starmap(bfs, [ (b,32) for b in blueprints[:3] ])
print("Part 2:", functools.reduce(lambda a,b:a*b, res))