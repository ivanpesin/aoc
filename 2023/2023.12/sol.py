#!/usr/bin/env python3

import sys, pprint, itertools, re, functools

data = [ s.strip().split() for s in open(sys.argv[1]).readlines() ]

@functools.cache
def arrangements(pat, groups, p, n):
    if p >= len(pat): return n == len(groups)

    res = 0
    if pat[p] in '.?': res = arrangements(pat, groups, p+1, n)

    if pat[p] in '#?':
        if n >= len(groups): return res
        q = p + groups[n]
        if q <= len(pat):
            if (q == len(pat) or pat[q] != '#') and '.' not in pat[p:q]:
                res += arrangements(pat, groups, q+1, n+1)

    return res

res = []
for line in data:
    pattern, groups = line[0], eval(line[1])
    if len(sys.argv) > 2: pattern, groups = '?'.join([line[0]]*5), eval(','.join([line[1]]*5))
    res.append(arrangements(pattern, groups, 0, 0))

print(sum(res))