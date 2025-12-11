#!/usr/bin/env python3

import sys, pprint, functools

net = {}
for s in open(sys.argv[1]):
    k, v = s.split()[0].strip(':'), s.split()[1:]
    net[k] = v

@functools.cache
def dfs(node, end):
    if node == end: return 1
    if node == 'out': return 0
    return sum(dfs(n, end) for n in net[node])

print("Part 1:", dfs('you', 'out'))
print("Part 2:", dfs('svr','fft') * dfs('fft','dac') * dfs('dac','out'))

