#!/usr/bin/env python3

import sys, functools

stones = open(sys.argv[1]).read().split()

@functools.lru_cache(maxsize=None)
def morph(stone, n):
    if n == 0: return 1
    if stone == '0': return morph('1', n-1)

    l = len(stone)
    if l % 2 == 0:
        a,b = str(int(stone[:l//2])), str(int(stone[l//2:]))
        return morph(a, n-1) + morph(b, n-1)

    return morph(str(int(stone)*2024), n-1)

print(sum(morph(s, int(sys.argv[2])) for s in stones))