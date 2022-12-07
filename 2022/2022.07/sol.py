#!/usr/bin/env python3

import sys, os, collections

with open(sys.argv[1]) as f: 
    data = [ l.strip() for l in f ]

dirs, cd = collections.defaultdict(int), ''
for l in data:
    token = l.split()
    if '$ cd ' in l: 
        if token[2] == '/': cd = '/'
        elif token[2] == '..': 
            sz = dirs[cd]
            if cd.count('/') == 1: cd = '/'
            else: cd = cd[:cd.rindex('/')]
            dirs[cd] += sz
        else: cd = os.path.join(cd, token[2])
        continue

    if token[0].isdigit(): dirs[cd] += int(token[0])

while cd != '/':
    sz = dirs[cd]
    if cd.count('/') == 1: cd = '/'
    else: cd = cd[:cd.rindex('/')]
    dirs[cd] += sz
   
p1 = 0
for d in dirs:
    if dirs[d] <= 100000: p1 += dirs[d]
print(f"Part 1: {p1}")

need = 30000000 - (70000000 - dirs['/'])
candidate = min([ (dirs[d],d) for d in dirs if dirs[d] >= need ])
print(f"Part 2: {candidate[0]}")