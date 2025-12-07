#!/usr/bin/env python3

import sys, functools

data = { (x,y): ch for y,s in enumerate(open(sys.argv[1]).readlines())
                   for x,ch in enumerate(s.strip('\n')) }
sx, sy = [ k for k,v in data.items() if v == 'S' ][0]
splitters = set()

@functools.cache
def trace(x,y):
    if (x,y) not in data: return 0
    while data.get((x,y),'') == '.': y += 1
    if data.get((x,y),'') == '^':
        splitters.add((x,y))
        return trace(x-1,y) + trace(x+1,y)
    return 1

p2 = trace(sx, sy+1)
print(f'Part 1: {len(splitters)}')
print(f'Part 2: {p2}')