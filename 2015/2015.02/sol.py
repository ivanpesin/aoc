#!/usr/bin/env python3

import sys

if __name__ == "__main__":

    with open(sys.argv[1]) as f:
        data = [ s.rstrip('\n') for s in f ]

    paper, ribbon = 0, 0
    for line in data:
        l,w,h = map(int, line.split('x'))

        extra = min([l*w, w*h, h*l])
        area  = 2*l*w + 2*w*h + 2*h*l

        bow = l * w * h
        rib = 2 * sum(sorted([l, w, h])[0:2])

        print(line, area + extra, rib + bow)
        paper += area + extra
        ribbon += rib + bow

    print("Part 1:", paper)
    print("Part 2:", ribbon)
