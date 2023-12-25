#!/usr/bin/env python3

import sys, pprint, re
from sympy import Symbol, Eq, solve

data = [ list(map(int, re.findall(r'(-?\d+)', s))) for s in open(sys.argv[1]) ]

lines = [ [ (x, y, z), (x+dx, y+dy, z+dz) ] for x, y, z, dx, dy, dz in data ]

def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b): return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0: return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

sign = lambda x: (1, -1)[x<0]

res = 0
for i in range(len(lines)):
    for j in range(i+1, len(lines)):
            p = line_intersection(lines[i], lines[j])

            if p is not None:
                found = False
                # if all(v >=7 and v <= 28 for v in p):
                if all(v >= 200_000_000_000_000 and v <= 400_000_000_000_000 for v in p):  found = True

                # check if the intersection happened in the past
                if (lines[i][0][0] > p[0] and sign(data[i][3]) > 0) or (lines[i][0][0] < p[0] and sign(data[i][3]) < 0) \
                   or (lines[i][0][1] > p[1] and sign(data[i][4]) > 0) or (lines[i][0][1] < p[1] and sign(data[i][4]) < 0):
                    found = False

                if (lines[j][0][0] > p[0] and sign(data[j][3]) > 0) or (lines[j][0][0] < p[0] and sign(data[j][3]) < 0) \
                   or (lines[j][0][1] > p[1] and sign(data[j][4]) > 0) or (lines[j][0][1] < p[1] and sign(data[j][4]) < 0):
                    found = False

                if found: res += 1

print("Part 1:", res)

params, times = {}, [Symbol(f't{i}') for i in range(3)] # 3 hails

for s in 'rpx rpy rpz rvx rvy rvz'.split(): params[s] = Symbol(s)

equations = []
for t, (px, py, pz, vx, vy, vz) in zip(times, data):
    equations += [
        Eq(px + vx * t, params['rpx'] + params['rvx'] * t),
        Eq(py + vy * t, params['rpy'] + params['rvy'] * t),
        Eq(pz + vz * t, params['rpz'] + params['rvz'] * t),
    ]

results = solve(equations, times + [ *params ], dict=True)
print(results)
print("Part 2:", results[0][params['rpx']] + results[0][params['rpy']] + results[0][params['rpz']])
