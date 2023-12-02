#!/usr/bin/env python3

import sys, pprint, math, collections

data = [ s.strip() for s in open(sys.argv[1]).readlines() ]

constraints = { 'red': 12, 'green': 13, 'blue': 14 }
game, possible, powers = [], [], []
for i, s in enumerate(data):
    game.append(collections.defaultdict(list))
    for draw in s.split(': ')[1].split('; '):
        for cubes in draw.split(', '):
            n, color = cubes.split(' ')
            game[i][color].append(int(n))

    if all(max(game[i][color]) <= constraints[color] for color in game[i]): possible.append(i+1)
    least = [ max(game[i][color]) for color in game[i] ]
    powers.append(math.prod(least))

# pprint.pp(game)
print("Part 1:", sum(possible))
print("Part 2:", sum(powers))