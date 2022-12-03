#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    data = f.read().split("\n\n")

elves = []
for cals in data:
    elves.append(sum(map(int, cals.splitlines())))

print(f"Part1: {max(elves)}")
print(f"Part2: {sum(sorted(elves)[-3:])}")