#!/usr/bin/env python3

import sys, os, collections

with open(sys.argv[1]) as f: 
    data = [ l.strip() for l in f ]

dirs, cd = collections.defaultdict(int), ''
for l in data:
    match l.split():
        case '$', 'cd', '/' : cd = '/'
        case '$', 'cd', '..':
            sz = dirs[cd]
            if cd.count('/') == 1: cd = '/'
            else: cd = cd[:cd.rindex('/')]
            dirs[cd] += sz
        case '$', 'cd', d   : cd = os.path.join(cd, d)
        case '$', 'ls'      : pass
        case 'dir', _       : pass
        case sz, _          : dirs[cd] += int(sz)

while cd != '/':
    sz = dirs[cd]
    if cd.count('/') == 1: cd = '/'
    else: cd = cd[:cd.rindex('/')]
    dirs[cd] += sz
   
p1 = sum(dirs[d] for d in dirs if dirs[d] <= 100_000)
print(f"Part 1: {p1}")

need = 300_000_00 - (70_000_000 - dirs['/'])
candidate = min([ (dirs[d],d) for d in dirs if dirs[d] >= need ])
print(f"Part 2: {candidate[0]}")