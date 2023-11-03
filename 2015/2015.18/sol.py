#!/usr/bin/env python3

import sys, pprint, copy

def simulate(data, i, max_i, part2=False):
    if part2: data[0,0] = data[0,max_i] = data[max_i,0] = data[max_i,max_i] = '#'

    for _ in range(i):
        new = {}
        for y in range(max_i+1):
            for x in range(max_i+1):
                n = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dx == dy == 0: continue
                        try:
                            if data[y+dy,x+dx] == '#': n += 1
                        except: pass

                if part2 and y in [0, max_i] and x in [0,max_i]: new[y,x] = '#'
                elif data[y,x] == '#':
                    if n == 2 or n == 3: new[y,x] = '#'
                    else: new[y,x] = '.'
                else:
                    if n == 3: new[y,x] = '#'
                    else: new[y,x] = '.'

        data = new

    return sum(1 for p in data if data[p] == '#')

with open(sys.argv[1]) as f:
    data, y, max_i = {}, 0, 0
    for s in f:
        for x, c in enumerate(s.rstrip()): data[y,x] = c
        max_i, y = len(s.rstrip())-1, y+1

print(simulate(copy.deepcopy(data), int(sys.argv[2]), max_i))
print(simulate(copy.deepcopy(data), int(sys.argv[2]), max_i, True))
