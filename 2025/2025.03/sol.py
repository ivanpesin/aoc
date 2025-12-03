#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    data = [ s.strip() for s in f ]

res, NO = 0, 12 if sys.argv[2] == '2' else 2
for s in data:
    a = [ int(c) for c in s ]
    s, lo = '', 0
    for i in range(NO-1, -1, -1):
        if i == 0: hi = len(a)
        else: hi = -i
        p, lo = max(a[lo:hi]), lo + a[lo:hi].index(max(a[lo:hi])) + 1
        s += str(p)
    res += int(s)

print(f'Result: {res}')