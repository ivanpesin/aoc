#!/usr/bin/env python3

import sys, pprint

steps = [ s.strip().split() for s in open(sys.argv[1]) ]

def list_vertices(edges):
    pos, perim = complex(0,0), 0
    vertices = [ pos ]
    for dir, l, _ in edges:
        l = int(l)
        perim += l
        match dir:
            case 'L': vertices.append(pos := pos - l)
            case 'R': vertices.append(pos := pos + l)
            case 'U': vertices.append(pos := pos - l*1j)
            case 'D': vertices.append(pos := pos + l*1j)

    return vertices, perim

def get_area(vertices):
    base, area = max(int(p.imag) for p in vertices), 0

    for i,v in enumerate(vertices):
        if i == 0: p = v; continue
        if v.imag == p.imag:
            l, h = int(p.real - v.real), base - p.imag
            area += h * l
        p = v

    return abs(int(area))

vertices, perim = list_vertices(steps)
print("Part 1:", get_area(vertices) + perim//2 + 1)

p2 = []
for _,_,code in steps:
    match code[7:8]:
        case '0': d = 'R'
        case '1': d = 'D'
        case '2': d = 'L'
        case '3': d = 'U'
    p2.append((d, int(code[2:7],16), code))

vertices, perim = list_vertices(p2)
print("Part 2:", get_area(vertices) + perim//2 + 1)
