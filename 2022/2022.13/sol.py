#!/usr/bin/env python3

import sys, pprint, functools

with open(sys.argv[1]) as f:
    data = f.read().split('\n\n')

def cmp(left, right):
    for i in range(len(left)):
        if i >= len(right): return 1
        if isinstance(left[i], int) and isinstance(right[i], int):
            if   left[i] < right[i]:  return -1
            elif left[i] > right[i]:  return 1
        elif isinstance(left[i], int):
            c = cmp([left[i]],right[i])
            if c != 0: return c
        elif isinstance(right[i], int):
            c = cmp(left[i],[right[i]])
            if c != 0: return c
        else:
            c = cmp(left[i],right[i])
            if c != 0: return c

    if len(left) < len(right): return -1
    return 0

p1, p2 = [], [ [[2]], [[6]] ]
for i,pair in enumerate(data):
    left, right = map(eval,pair.splitlines())
    p1.append((i+1,cmp(left,right)))
    p2.extend([left,right])
    
print(f"Part 1: {sum(v[0] for v in p1 if v[1] < 0)}")

p2.sort(key=functools.cmp_to_key(cmp))
print(f"Part 2: {(p2.index([[2]])+1) * (p2.index([[6]])+1)}")