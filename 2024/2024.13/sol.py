#!/usr/bin/env python3

import sys, re, pprint, collections
from sympy import solve, symbols

machines = []
for block in open(sys.argv[1]).read().split('\n\n'):
    machines.append([])
    for line in block.splitlines():
        machines[-1].append(list(map(int, re.findall(r'(-?\d+)', line))))

def puzzle(part2=False):
    res = 0
    for m in machines:
        ax, ay, bx, by, tx, ty = *m[0],  *m[1], *m[2]

        if part2:
            tx += 10000000000000
            ty += 10000000000000

        a, b = symbols('a b', integer=True)
        solution = solve(
            [a * ax + b * bx - tx, a * ay + b * by - ty],
            [a, b],
        )
        if solution: res += solution[a] * 3 + solution[b]
    return res

print("Part 1:", puzzle(part2=False))
print("Part 2:", puzzle(part2=True))