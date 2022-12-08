#!/usr/bin/env python3

import sys, pprint

with open(sys.argv[1]) as f: 
    data = [ l.strip() for l in f ]

visible, score = len(data)*4-4, {}
for row in range(1,len(data)-1):
    for col in range(1,len(data)-1):
        height, v = int(data[row][col]), False
        if max(map(int,list(data[row][:col]))) < height: v = True
        elif max(map(int,list(data[row][col+1:]))) < height: v = True
        elif max(int(data[i][col]) for i in range(len(data)) if i < row) < height: v = True
        elif max(int(data[i][col]) for i in range(len(data)) if i > row) < height: v = True
        if v: visible += 1

        s = [0,0,0,0]
        for delta in range(1,col+1):
            s[0] += 1
            if int(data[row][col-delta]) >= height: break
        for c in range(col+1,len(data)):
            s[1] += 1
            if int(data[row][c]) >= height: break
        for delta in range(1,row+1):
            s[2] += 1
            if int(data[row-delta][col]) >= height: break
        for r in range(row+1,len(data)):
            s[3] += 1
            if int(data[r][col]) >= height: break
        score[row,col] = s[0]*s[1]*s[2]*s[3]

print(f"Part 1: {visible}")
print(f"Part 2: {sorted((score[s],s) for s in score)[-1][0]}")