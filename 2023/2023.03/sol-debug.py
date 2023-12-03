#!/usr/bin/env python3

import sys, pprint
import re

data = [ s.strip() for s in open(sys.argv[1]).readlines() ]

def part1():
    res = []
    for i, s in enumerate(data):
        print(s, end=' ')
        for m in re.finditer(r'\d+', s):
            start, end, adj = m.start(), m.end(), []
            print(f"{m.group()}@({start},{end})", end=' ')
            if start > 0:
                start -= 1
                adj.append(s[start])
            if end < len(s):
                end += 1
                adj.append(s[end-1])
            if i > 0: adj.extend(data[i-1][start:end])
            if i < len(data)-1: adj.extend(data[i+1][start:end])

            print(f"adj={adj}", end=' ')
            adj = [ c for c in adj if not (c.isdigit() or c=='.') ]
            if adj:
                print("Y", end=' ')
                res.append(int(m.group()))
        print()

    return sum(res)

def part2():
    res = []
    for i, s in enumerate(data):
        for m in re.finditer(r'\*', s):
            pos, adj = m.start(), []

            for j in range(i-1, i+2):
                if j < 0 or j >= len(data): continue
                for a in re.finditer(r'\d+', data[j]):
                    if (pos-1 <= a.start() <= pos+1) or (pos-1 < a.end() <= pos+2) or (a.start() < pos-1 and a.end() > pos+2):
                        adj.append(int(a.group()))

            if len(adj) == 2: res.append(adj[0] * adj[1])

    return sum(res)

print("Part 1:", part1())
print("Part 2:", part2())