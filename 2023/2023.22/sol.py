#!/usr/bin/env python3

import sys, pprint, copy

data = [ [list(map(int, a.split(','))), list(map(int,b.split(',')))] for a,b in [ s.strip().split('~') for s in open(sys.argv[1]) ]]
data.sort(key=lambda x: min(x[0][2], x[1][2]))

space, blocks = {}, []
for i, block in enumerate(data):
    b = []
    for x in range(block[0][0], block[1][0]+1):
        for y in range(block[0][1], block[1][1]+1):
            for z in range(block[0][2], block[1][2]+1):
                space[(x,y,z)] = i
                b.append((x,y,z))
    blocks.append(b)

def jenga(space,blocks,detect=False):
    changed, moved, n = True, 0, 0
    while changed:
        changed, n = False, n+1
        if detect and n > 1: return moved
        for i, block in enumerate(blocks):
            if block is None: continue
            if any(a[2]==1 for a in block): continue

            stable = False
            for a in block:
                a = (a[0], a[1], a[2]-1)
                if a in space and space[a] != i:
                    stable = True
                    continue
            if stable: continue

            changed, newblock = True, []
            for a in block:
                del space[a]
                newblock.append((a[0], a[1], a[2]-1))
            for a in newblock: space[a] = i
            blocks[i], moved = newblock, moved+1

    return moved

# print(" -- Initial fall")
jenga(space, blocks)

p1 = p2 = 0
for i in range(len(blocks)):
    cblocks, cspace = copy.deepcopy(blocks), space.copy()
    # print(f" -- Removing block {i} {chr(65+i)}")
    cblocks[i] = None
    for p in blocks[i]: del cspace[p]

    m = jenga(cspace, cblocks, detect=True)
    if m == 0: p1 += 1
    p2 += m

print(f"Part 1: {p1}\nPart 2: {p2}")
