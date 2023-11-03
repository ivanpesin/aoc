#!/usr/bin/env python3

import sys, pprint, itertools

def solve(people: list):
    perm  = itertools.permutations(people[:-1])
    bracelets = []
    for p in perm:
        if p.index(people[1]) < p.index(people[0]):
            bracelets.append(p + (people[-1],))
    # pprint.pp(bracelets)

    max_happiness = 0
    for p in bracelets:
        happiness = 0
        for i in range(len(p)):
            happiness += happiness_map[(p[i], p[(i+1)%len(p)])] + happiness_map[(p[(i+1)%len(p)], p[i])]
        max_happiness = max(max_happiness, happiness)

    return max_happiness

if __name__ == "__main__":

    happiness_map = {}
    with open(sys.argv[1]) as f:
        for l in f:
            info = l.strip('.\n').split(' ')
            happiness_map[(info[0], info[-1])] = int(info[3]) if info[2] == 'gain' else -int(info[3])

    people = list(set([k[0] for k in happiness_map]))
    for p in people: happiness_map[('me', p)] = happiness_map[(p, 'me')] = 0
    # pprint.pp(happiness_map)

    # this is called a "bracelet" enumeration problem: https://math.stackexchange.com/questions/4565119/bracelet-enumeration
    print("Part 1:", solve(people))
    print("Part 2:", solve(people + ['me']))
