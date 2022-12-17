#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    jets = list(f.readline().strip())

shapes = [
    {(0,0):'#',(1,0):'#',(2,0):'#',(3,0):'#'},
    {(0,1):'#',(1,0):'#',(1,1):'#',(1,2):'#',(2,1):'#'},
    {(0,0):'#',(1,0):'#',(2,0):'#',(2,1):'#',(2,2):'#'},
    {(0,0):'#',(0,1):'#',(0,2):'#',(0,3):'#'},
    {(0,0):'#',(0,1):'#',(1,0):'#',(1,1):'#'},
]

WIDTH, SDX, SDY = 7, 2, 3

def can_move(shi,dx,dy):
    for x,y in shapes[shi]:
        nx,ny = x+dx,y+dy
        if ny < 0 or not -1 < nx < WIDTH: return False
        if (nx,ny) in chamber: return False
    return True

def fall(nshape, part):
    global tick, keep_until

    if chamber: 
        h = max(k[1] for k in chamber) + 1
        x, y = SDX, SDY + h
    else: h, x, y = -1, SDX, SDY
    ishape, atrest = nshape % len(shapes), False

    if part == 2:
        profile = [ max([-1] + [k[1] for k in chamber if k[0] == a]) for a in range(WIDTH) ]
        base = min(profile)
        profile = [ n - base for n in profile ]
        shash = (ishape, tick % len(jets), profile)
        if state.count(shash) == 2:
            cstart  = state.index(shash)
            clen    = (nshape - cstart)//2
            cheight = height[cstart+clen]-height[cstart]
            cfit    = (1_000_000_000_000-cstart)//clen
            brem    = 1_000_000_000_000-cstart-(1_000_000_000_000-cstart)//clen*clen
            print(f'  cycle  start: {cstart} end: {cstart+clen} h(start): {height[cstart]} h(end): {height[cstart+clen]}')
            print(f'  cycle  len: {clen} h(cycle): {cheight}')
            print(f'  cycles fit: {cfit}')
            print(f'  remaining blocks: {brem}')
            print(f'Part 2: {height[cstart] + (cheight * cfit) + (height[cstart+brem]-height[cstart])}')
            return           

        state.append(shash); height.append(h)

    while not atrest:
        move = jets[tick % len(jets)]
        if   move == '>' and can_move(ishape,x+1,y): x += 1
        elif move == '<' and can_move(ishape,x-1,y): x -= 1

        if can_move(ishape,x,y-1): y -= 1
        else: 
            atrest = True
            for a,b in shapes[ishape]: chamber[x+a,y+b] = '#'

        # trim the older lines, a significant speed up; 100 is an empirical length
        if keep_until < y - 100:
            for i in range(keep_until, y-100):
                for k in [e for e in chamber if e[1]==i]: del chamber[k]
            keep_until = y - 100
            
        tick += 1

chamber, tick, keep_until, state, height = {}, 0, 0, [], []
for n in range(2022): fall(n, 1)
print(f"Part 1: {max(k[1] for k in chamber) + 1}")

chamber, tick, keep_until, state, height = {}, 0, 0, [], []
for n in range(int(sys.argv[2])): fall(n, 2)