#!/usr/bin/env python3

import sys, math

house, p2 = 0, False
while True:
    house, presents, p2_presents = house + 1, 0, 0
    visitors = set([1, house])
    for elf in range(1, int(math.sqrt(house)) + 1):
        if house % elf == 0: visitors.update([elf, house // elf])
    if not p2: presents = sum(visitors) * 10
    for v in visitors:
        if v * 50 >= house: p2_presents += v * 11

    if presents >= int(sys.argv[1]):
        print("Part 1", house, presents)
        p2 = True
    if p2_presents >= int(sys.argv[1]):
        print("Part 2", house, p2_presents)
        break
    # if house % 1000 == 0: print(house, presents)

