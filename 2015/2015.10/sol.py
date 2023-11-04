#!/usr/bin/env python3

import sys, itertools

s = open(sys.argv[1]).readline().rstrip('\n')

for i in range(40):
    s = ''.join([ str(len(list(g))) + k for k, g in itertools.groupby(s) ])
print("Part 1:", len(s))

for i in range(10):
    s = ''.join([ str(len(list(g))) + k for k, g in itertools.groupby(s) ])
print("Part 2:", len(s))