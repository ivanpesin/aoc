#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    data = { s.strip().split(': ')[0]:s.strip().split(': ')[1] for s in f }

def monkey(m):
    assert m in data
    if data[m].isdigit(): return int(data[m])
    
    a,op,b = data[m].split()
    return eval(f"{monkey(a)} {op} {monkey(b)}")

print("Part 1:", monkey(sys.argv[2]))

a, op, b = data['root'].split()
target = monkey(b)

if len(sys.argv) > 3:
    data['humn'] = sys.argv[3]
    print(f"a={monkey(a)} b={monkey(b)}")
else:
    def bsearch(v,lo,hi):
        if hi < lo: return -1

        mid = (hi+lo)//2
        data['humn'] = str(mid)
        m = monkey(a)
        if m == v: return mid
        if m > v: return bsearch(v,mid+1,hi)
        return bsearch(v,lo,mid-1)

    print("Part 2:", bsearch(monkey(b),1000000000000,10000000000000))