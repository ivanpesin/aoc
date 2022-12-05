#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f: 
    data = f.read().split("\n\n")

def init_stacks():
    stacks = []
    for l in data[0].splitlines():
        if l[1].isdigit(): break
        for i in range(1,len(l)-1,4):
            if len(stacks) < i//4+1: stacks.append([])
            if l[i] != ' ': stacks[i//4].insert(0,l[i])
    return stacks

# --- part 1
stacks = init_stacks()

for l in data[1].splitlines():
    cnt, fr, to = list(map(int,filter(str.isdigit,l.split())))

    for _ in range(cnt):
        stacks[to-1].append(stacks[fr-1].pop())

print("Part 1:",''.join([s[-1] for s in stacks]))

# --- part 2
stacks = init_stacks()

for l in data[1].splitlines():
    cnt, fr, to = list(map(int,filter(str.isdigit,l.split())))

    stacks[to-1].extend(stacks[fr-1][-cnt:])
    stacks[fr-1] = stacks[fr-1][:-cnt]

print("Part 2:",''.join([s[-1] for s in stacks]))
