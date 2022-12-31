#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    data = [ int(s) for s in f ]

def decrypt(vals, order):
    L = len(vals)
    ptrs = list(range(L))

    for i in order:
        pos  = ptrs.index(i)
        ptrs = ptrs[:pos] + ptrs[pos+1:]
        npos = (pos + vals[i]) % (L-1)
        if npos == 0: npos = L
        ptrs = ptrs[:npos] + [i] + ptrs[npos:]

    z = ptrs.index(vals.index(0))
    return sum(vals[ptrs[(z+p)%L]] for p in (1000,2000,3000))

print("Part 1:",decrypt(data, range(len(data))))
print("Part 2:",decrypt([d * 811589153 for d in data], list(range(len(data))) * 10))