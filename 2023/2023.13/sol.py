#!/usr/bin/env python3

import sys, pprint, itertools, re, functools

imgs = open(sys.argv[1]).read().split('\n\n')

def mirrored_at(cols, v):
    res = []
    for c in range(1,cols):
        if v[c-1] == v[c]:
            for i in range(1, min(c,cols-c)):
                if v[c-1-i] != v[c+i]: break
            else: res.append(c)
    return res if res else [0]

p1 = p2 = 0
for img in imgs:
    a = { (r,c):ch for r,s in enumerate(img.split('\n'))
                   for c,ch in enumerate(s) }
    rows, cols = max(r for r,_ in a) + 1, max(c for _,c in a) + 1

    v = [ [ a[r,c] for r in range(rows) ] for c in range(cols) ]
    vfolds = mirrored_at(cols, v)
    v = [ [ a[r,c] for c in range(cols-1,-1,-1) ] for r in range(rows) ]
    hfolds = mirrored_at(rows, v)
    p1 += vfolds[0] + hfolds[0]*100
    assert vfolds[0] != 0 or hfolds[0] != 0, "No reflection found!"

    # part 2
    for y,x in a:
        a[y,x] = '#' if a[y,x] == '.' else '.' # flip

        v = [ [ a[r,c] for r in range(rows) ] for c in range(cols) ]
        new_fold = list(set(mirrored_at(cols, v)) - set(vfolds))
        if new_fold and new_fold[0] > 0:
            p2 += new_fold[0]
            break

        v = [ [ a[r,c] for c in range(cols-1,-1,-1) ] for r in range(rows) ]
        new_fold = list(set(mirrored_at(rows, v)) - set(hfolds))
        if new_fold and new_fold[0] > 0:
            p2 += new_fold[0]*100
            break
        a[y,x] = '#' if a[y,x] == '.' else '.'

print("Part 1:", p1 )
print("Part 2:", p2 )