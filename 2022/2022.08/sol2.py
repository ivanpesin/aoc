#!/usr/bin/env python3

import sys, math

with open(sys.argv[1]) as f: 
    data = [ [int(c) for c in l.strip()] for l in f ]

sz = len(data)
visible, score = sz*4-4, {}
for row in range(1, sz-1):
    for col in range(1, sz-1):
        height = data[row][col]
        if max(data[row][:col]) < height    : visible += 1
        elif max(data[row][col+1:]) < height: visible += 1
        elif max(data[i][col] for i in range(sz) if i < row) < height: visible += 1
        elif max(data[i][col] for i in range(sz) if i > row) < height: visible += 1

        s = {}
        for dir in [(-1,0),(1,0),(0,-1),(0,1)]:
            pos = [ sum(pair) for pair in zip((row,col), dir) ]
            while min(pos) >= 0 and max(pos) < sz:
                if dir in s: s[dir] += 1
                else: s[dir] = 1
                if data[pos[0]][pos[1]] >= height: break
                pos = [ sum(pair) for pair in zip(pos, dir) ]

        score[row,col] = math.prod(s.values())

print(f"Part 1: {visible}")
print(f"Part 2: {max(score.values())}")