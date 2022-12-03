#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f:
    data = [ l.strip().split() for l in f ]

score = 0
for pair in data:
        opp, you = pair
        opp, you = ord(opp)-ord('A')+1, ord(you)-ord('X')+1

        score += you
        if you == opp: score += 3
        elif (you - opp == 1) or \
                (you == 1 and opp == 3): score += 6

print(f"Part 1: {score}")

score = 0
for pair in data:
        opp, result = pair
        opp = ord(opp)-ord('A')+1

        if result   == 'X': # lose
            you = 3
            if opp > 1: you = opp - 1
        elif result == 'Z': # win
            you = 1
            if opp < 3: you = opp + 1
            score += 6
        else: # draw
            you = opp
            score += 3
        score += you

print(f"Part 2: {score}")
