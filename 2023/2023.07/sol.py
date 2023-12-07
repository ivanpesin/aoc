#!/usr/bin/env python3

import sys, collections, pprint

data = [ [s.split()[0],int(s.split()[1])] for s in open(sys.argv[1]).readlines() ]

def sort_hands(part2, key):
    res = []

    c, cnt = [], collections.Counter(key)
    for a in cnt.most_common():
        if part2 and a[0] == 'J': continue
        c.append(a[1])
    while len(c) < 2: c.append(0)
    high, low, joker = c[0], c[1], cnt.get('J', 0) if part2 else 0
    if high + joker == 5: res.append(7)
    elif high + joker == 4: res.append(6)
    elif high + joker == 3 and low == 2: res.append(5)
    elif high + joker == 3: res.append(4)
    elif high + joker == 2 and low == 2: res.append(3)
    elif high + joker == 2: res.append(2)
    else: res.append(1)

    order = 'J23456789TQKA' if part2 else '23456789TJQKA'
    res.extend([ order.index(c) for c in key ])
    return res

for part2 in [False, True]:
    data.sort(key=lambda x: sort_hands(part2, x[0]))
    print("Part 2:" if part2 else "Part 1:", sum((i+1) * d[1] for i,d in enumerate(data)))