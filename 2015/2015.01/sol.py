#!/usr/bin/env python3

import sys

if __name__ == "__main__":

    with open(sys.argv[1]) as f:
        data = [ s.rstrip('\n') for s in f ]

    for l in data:
        print("Part 1:", l.count('(') - l.count(')'))

        floor = 0
        for n, c in enumerate(l):
            if c == '(':    floor += 1
            else:           floor -= 1

            if floor == -1:
                print("Part 2:", n+1)
                break