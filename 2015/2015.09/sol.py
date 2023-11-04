#!/usr/bin/env python3

import sys, pprint

if __name__ == "__main__":

    with open(sys.argv[1]) as f:
        data = [ s.rstrip('\n').split() for s in f ]

    dist = {}
    cities = set()
    for d in data:
        dist[(d[0], d[2])] = dist[(d[2], d[0])] = int(d[4])
        cities |= set([d[0], d[2]])

    paths = []
    for c in cities:
        paths.append((c, 0, [c])) # start, distance, path

    travel_length = []
    while paths:
        p = paths.pop(0)
        if len(p[2]) == len(cities):
            travel_length.append(p)
            continue
        for c in cities - set(p[2]):
            paths.append((c, p[1] + dist[(p[0], c)], p[2] + [c]))

    print("Part 1:", min([ (p[1],p[2]) for p in travel_length ]))
    print("Part 2:", max([ (p[1],p[2]) for p in travel_length ]))    