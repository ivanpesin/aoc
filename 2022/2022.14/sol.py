#!/usr/bin/env python3

import sys, re, collections, pprint

with open(sys.argv[1]) as f:
    data = [ list(map(int,re.findall(r'\d+', l))) for l in f ]

part = int(sys.argv[2])
grid = collections.defaultdict(lambda: '.')
sign = lambda k: -1 if k < 0 else 1

frm = [ 500,0 ]
lo, hi = [ *frm ], [ *frm ]

for l in data:
    for k in range(0,len(l)-2,2):
        a, b, x, y = l[k:k+4]
        if a == x:
            for i in range(b,y+sign(y-b),sign(y-b)): grid[x,i] = '#'
        else:
            for i in range(a,x+sign(x-a),sign(x-a)): grid[i,y] = '#'
        if not lo: lo = [a,b]
        if not hi: hi = [x,y]
        lo = [ min([a,x,lo[0]]), min([b,y,lo[1]]) ]
        hi = [ max([a,x,hi[0]]), max([b,y,hi[1]]) ]

done = False
while not done:
    x,y, atrest = *frm, False
    while not atrest:
        for a,b in [(0,1),(-1,1),(1,1)]:
            if grid[x+a,y+b] == '.' and y < hi[1]+1: 
                x,y = x+a,y+b
                break
        else:
            atrest = True
            grid[x,y] = 'o'
        if ((part == 1 and y > hi[1]) or (part == 2 and grid[500,0] == 'o')):
            done = True
            break

print(sum(1 for v in grid.values() if v =='o'))