#!/usr/bin/env python3

import sys, pprint, re, math, time, collections

robots = []
for s in open(sys.argv[1]):
    x,y, dx,dy = [int(a) for a in re.findall(r'(-?\d+)', s) ]
    robots.append((complex(x, y), complex(dx, dy)))

W, H = 11, 7
W, H = 101, 103
MW, MH = W//2, H//2

def print_map(robots, coords, tick):
    print("\033[H\033[J", end='', flush=True)
    for y in range(H):
        for x in range(W):
            if (x+y*1j) in coords: print(coords[(x+y*1j)], end='')
            else:                  print('.', end='')
        print(f" step = {tick+1}")

for tick in range(int(sys.argv[2])):
    coords = collections.defaultdict(int)
    for i in range(len(robots)):
        pos, vel = robots[i]
        npos = pos + vel
        if npos.real not in range(W): npos = npos.real % W + npos.imag*1j
        if npos.imag not in range(H): npos = npos.real + (npos.imag % H)*1j
        robots[i] = npos, vel
        coords[npos] += 1

    if sys.argv[3] == '2':
        for c in coords:
            if all(c+d in coords for d in (-2,-1,1,2,-2j,-1j,1j,2j)):
                print_map(robots, coords, tick)

if sys.argv[3] == '1':
    res = {'TL': 0, 'TR': 0, 'BL': 0, 'BR': 0}
    for r in sorted(robots, key=lambda r: (r[0].imag, r[0].real)):
        pos = r[0]
        if pos.real in range(MW) and pos.imag in range(MH): res['TL'] += 1
        if pos.real in range(MW+1, W) and pos.imag in range(MH): res['TR'] += 1
        if pos.real in range(MW) and pos.imag in range(MH+1, H): res['BL'] += 1
        if pos.real in range(MW+1, W) and pos.imag in range(MH+1, H): res['BR'] += 1

    print("Part 1:", math.prod(res.values()))