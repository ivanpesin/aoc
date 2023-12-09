#!/usr/bin/env python3

import sys, re

data = [ list(map(int, re.findall(r'-?\d+', s))) for s in open(sys.argv[1]) ]

def predict(seq):
    deltas = [ seq ]
    while not all([x == 0 for x in deltas[-1]]):
        s = deltas[-1]
        deltas.append([])
        for pair in zip(s, s[1:]): deltas[-1].append(pair[1] - pair[0])
        s = deltas[-1]

    deltas[-1].append(0)
    for i in range(len(deltas)-2, -1, -1): deltas[i].append(deltas[i+1][-1] + deltas[i][-1])

    deltas[-1].insert(0, 0)
    for i in range(len(deltas)-2, -1, -1): deltas[i].insert(0, deltas[i][0] - deltas[i+1][0])

    return deltas[0][0], deltas[0][-1]

head, tail = [], []
for seq in data:
    left, right = predict(seq[:])
    head.append(left)
    tail.append(right)

print("Part 1:", sum(tail))
print("Part 2:", sum(head))