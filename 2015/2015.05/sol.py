#!/usr/bin/env python3

import sys, pprint

def part1(data):
    nice = 0
    for s in data:
        if len(list(filter(lambda x: x in 'aeiou', s))) >= 3 and \
           any(map(lambda x: x[0] == x[1], zip(s, s[1:]))) and \
           not any(map(lambda x: x in s, ['ab', 'cd', 'pq', 'xy'])):
            nice += 1
        
    print("Part 1:", nice)

def part2(data):
    nice = 0
    for s in data:
        if any(map(lambda x: x[0] == x[1], zip(s, s[2:]))) and \
            list(filter(lambda x: s.count(''.join(x)) > 1, zip(s, s[1:]))):
            nice += 1

    print("Part 2:", nice)

if __name__ == "__main__":

    with open(sys.argv[1]) as f:
        data = [ s.rstrip('\n') for s in f ]

    part1(data.copy())
    part2(data.copy())
