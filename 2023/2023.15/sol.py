#!/usr/bin/env python3

import sys, pprint, re, collections

data = open(sys.argv[1]).readline().strip().split(',')

def hash(s, res=0):
    for c in s: res = (res + ord(c)) * 17 % 256
    return res

print("Part 1:", sum(hash(step) for step in data))

boxes = collections.defaultdict(list)
for step in data:
    label, op, flen = re.split(r'([-=])', step)
    n = hash(label)
    if   op == '-': boxes[n] = [ (l,f) for l,f in boxes[n] if l != label ]
    elif op == '=':
        replace = [ i for i in range(len(boxes[n])) if boxes[n][i][0] == label ]
        if replace: boxes[n][replace[0]] = (label,int(flen))
        else: boxes[n].append((label,int(flen)))

print("Part 2:", sum(
    [ sum([(i+1) * (j+1) * boxes[i][j][1] for j in range(len(boxes[i]))])
        for i in boxes if boxes[i] ]))