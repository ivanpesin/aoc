#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    data = [ list(s.strip()) for s in f ]

ORDER = {'=':-2, '-':-1, '0':0, '1':1, '2':2 }

def snafu2dec(n):
    res = 0
    for i,d in enumerate(n[::-1]): res += ORDER[d]*5**i
    return res

def dec2snafu(n):
    res = []
    while n > 0:
        n, r = divmod(n, 5)
        if   r < 3:  res.append(str(r))
        else:
            n += 1
            if   r == 3: res.append('='); 
            elif r == 4: res.append('-'); 
    return ''.join(res[::-1])

s = sum(snafu2dec(d) for d in data)
print("Sum:",s)
print("In SNAFU:",dec2snafu(s))