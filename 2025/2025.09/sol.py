#!/usr/bin/env python3

import sys, pprint, itertools as it
import functools

tiles = [ eval(s) for s in open(sys.argv[1]).readlines() ]
sides = list(it.pairwise(tiles + tiles[:1]))

@functools.cache
def point_inside(p):
    x,y = p
    inside = False

    for s in sides:
        a,b = s
        # check if point is on the edge
        if a[1] == b[1] == y and min(a[0],b[0]) <= x <= max(a[0],b[0]): return True
        if a[0] == b[0] == x and min(a[1],b[1]) <= y <= max(a[1],b[1]): return True
        # ray-cast if point is inside
        if (a[1] > y) != (b[1] > y):
            slope = (b[0]-a[0]) / (b[1]-a[1])
            xint = a[0] + slope * (y - a[1])
            if xint == x:   return True
            if xint > x:    inside = not inside
    return inside

@functools.cache
def intersect(a,b):
    a_is_vertical = a[0][0] == a[1][0]
    b_is_vertical = b[0][0] == b[1][0]
    # both vertical or both horizontal -> no intersection
    if a_is_vertical == b_is_vertical: return False

    if a_is_vertical:
        x,y = a[0][0], b[0][1]
        ay1, ay2 = sorted((a[0][1], a[1][1]))
        bx1, bx2 = sorted((b[0][0], b[1][0]))
        return bx1 < x < bx2 and ay1 < y < ay2
    else:
        x, y = b[0][0], a[0][1]
        by1, by2 = sorted((b[0][1], b[1][1]))
        ax1, ax2 = sorted((a[0][0], a[1][0]))
        return ax1 < x < ax2 and by1 < y < by2

def rect_inside(rect):
    # check all corners are inside the shape
    for p in rect:
        if not point_inside(p): return False
    # check no edges intersect shape sides
    edges = [(rect[i], rect[(i + 1) % 4]) for i in range(4)]
    for r in edges:
        for s in sides:
            if intersect(r, s): return False
    return True

p1 = p2 = 0
for a,b in it.combinations(tiles, 2):
    c, d = (a[0], b[1]), (b[0], a[1])
    area = (abs(a[0]-b[0])+1) * (abs(a[1]-b[1])+1)
    p1 = max(p1, area)
    if area > p2 and rect_inside([a, c, b, d]):
        p2 = max(p2, area)

print("Part 1:", p1)
print("Part 2:", p2)