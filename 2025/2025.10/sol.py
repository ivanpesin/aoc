#!/usr/bin/env python3

import sys, pprint, itertools as it
from scipy.optimize import linprog

desired, buttons, joltage = [], [], []
for s in open(sys.argv[1]):
    desired.append([ c == '#' for c in s.split()[0][1:-1] ])
    buttons.append([ eval(x[:-1] + ',)') for x in s.split()[1:-1] ])
    joltage.append(eval(s.split()[-1][1:-1]))

def press(l, buttons):
    state = [False] * l
    for b in buttons:
        for i in b: state[i] = not state[i]
    return state

p1 = p2 = 0
for i, light in enumerate(desired):
    for j in range(1,10):
        done = False
        for c in it.combinations(buttons[i], j):
            if press(len(light), c) == light:
                done, p1 = True, p1 + j
                break
        if done: break

    # min c x, such that Ax = joltage
    A, c = [], [1] * len(buttons[i])
    for j in range(len(joltage[i])):
        A.append([ int(j in b) for b in buttons[i] ])
    p2 += int(sum(linprog(c, A_eq=A, b_eq=joltage[i], integrality=1).x))

print(f'Part 1: {p1}')
print(f'Part 2: {p2}')

