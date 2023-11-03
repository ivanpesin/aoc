#!/usr/bin/env python3

import sys, pprint, copy

def simulate(data, gens, part2=False):
    if part2:
        data[0][0] = data[0][len(data[0])-1] = '#'
        data[len(data)-1][0] = data[len(data)-1][len(data[0])-1] = '#'
    for _ in range(gens):
        new = []
        for y in range(len(data)):
            new.append([])
            for x in range(len(data[y])):
                n = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dx == 0 and dy == 0: continue
                        if y+dy < 0 or y+dy >= len(data): continue
                        if x+dx < 0 or x+dx >= len(data[y]): continue
                        if data[y+dy][x+dx] == '#': n += 1
                # print(f"{y=},{x=} | {data[y][x]} {n=}")
                if part2 and (y == 0 or y == len(data)-1) and (x == 0 or x == len(data[y])-1): new[y].append('#')
                elif data[y][x] == '#':
                    if n == 2 or n == 3: new[y].append('#')
                    else: new[y].append('.')
                else:
                    if n == 3: new[y].append('#')
                    else: new[y].append('.')
        data = new

    return sum(r.count("#") for r in data)


with open(sys.argv[1]) as f:
    data = [ list(s.rstrip('\n')) for s in f ]

pprint.pp(data)

print(simulate(copy.deepcopy(data), int(sys.argv[2])))
print(simulate(copy.deepcopy(data), int(sys.argv[2]), True))