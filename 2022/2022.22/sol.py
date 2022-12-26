#!/usr/bin/env python3

import sys, re

with open(sys.argv[1]) as f:
    data, moves = f.read().split('\n\n')

TURNS = { "L": { (0,1): (-1,0), (-1,0): (0,-1), (0,-1): (1,0), (1,0): (0,1) },
          "R": { (0,1): (1,0), (1,0): (0,-1), (0,-1): (-1,0), (-1,0): (0,1) } }
HSCORE = { (0,1): 0, (1,0): 1, (0,-1): 2, (1,0): 3 }
data, moves = data.splitlines(), re.findall(r"\d+|[LR]", moves)
H, W = len(data), max(len(l) for l in data)
pos, head = [ 0, data[0].index('.') ], (0,1)

for move in moves:
    # print("Moving",pos,head,move)
    if move in ('L','R'):
        head = TURNS[move][head]
        continue
    for step in range(int(move)):
        void = True
        nr, nc = pos
        while void:
            nr, nc = (nr + head[0])%H, (nc + head[1])%W
            if nc < len(data[nr]) and data[nr][nc] != ' ': void = False
        if data[nr][nc] == '#': break
        pos = [nr,nc]

print("Pos:",pos,"Head:",head)
print("Part 1:",(pos[0]+1)*1000 + (pos[1]+1)*4 + HSCORE[head])
