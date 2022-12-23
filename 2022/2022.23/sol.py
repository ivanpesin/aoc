#!/usr/bin/env python3

import sys
from itertools import product

with open(sys.argv[1]) as f:
    elves = set( (r,c) for r,s in enumerate(f.readlines()) for c in range(len(s.strip())) if s[c] == '#' )

N, S, W, E = (-1,0), (1,0), (0,-1), (0,1)
ORDER = [ N, S, W, E ]

for round in range(int(sys.argv[2])):
    # print("Round:",round,"Elves:", elves)
    prev = elves
    plan = {}
    for elf in elves:
        r,c = elf

        for a,b in product((-1,0,1),(-1,0,1)):
            if a == b == 0: continue
            if (r+a,c+b) in elves: break
        else:
            continue


        for o in range(len(ORDER)):
            head, done = ORDER[(o+round)%len(ORDER)], True
            for i in range(-1,2):
                if head[0] != 0: cpos = (r+head[0],c+i)
                else:            cpos = (r+i,c+head[1])
                if cpos in elves:
                    done = False
                    break
            if done:
                if (r+head[0],c+head[1]) in plan:
                    # print("    collision:",elf,"to",(r+head[0],c+head[1]))
                    del plan[(r+head[0],c+head[1])]
                else:
                    # print("   ",elf,"to",(r+head[0],c+head[1]))
                    plan[(r+head[0],c+head[1])] = elf
                break

    # print("  Plan:",plan)

    moved = set()
    for p in plan:
        elves.discard(plan[p])
        moved.add(p)
    elves = moved | elves

    if elves == prev:
        print("Part 2:",round+1)
        break
    

frm = min(c[0] for c in elves), min(c[1] for c in elves)
to  = max(c[0] for c in elves), max(c[1] for c in elves)

# print("  Final:",elves)
res = '\n'.join([ ''.join([ '#' if (r,c) in elves else '.' for c in range(frm[1],to[1]+1) ]) for r in range(frm[0],to[0]+1) ])
# print(res)
print(res.count('.'))
