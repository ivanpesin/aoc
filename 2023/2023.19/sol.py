#!/usr/bin/env python3

import sys, pprint, math

workflows, ratings = [ block.splitlines() for block in open(sys.argv[1]).read().split('\n\n') ]

wf, res = {}, 0
for name,desc in [a.split('{') for a in workflows]:
    wf[name] = [ a.split(':') for a in desc[:-1].split(',') ]

for rat in ratings:
    v = { a.split('=')[0]:int(a.split('=')[1]) for a in rat[1:-1].split(',') }
    chain,x,m,a,s = 'in', v['x'],v['m'],v['a'],v['s']
    while chain not in ['A','R']:
        for r in wf[chain]:
            if len(r) == 2 and eval(r[0]): chain = r[1]; break
            if len(r) == 1:                chain = r[0]; break
    if chain == 'A': res += x+m+a+s

print("Part 1:", res)

# Part 2 - find all accepted paths
accepted, stack = [], [ ('in', []) ]
while stack:
    chain, conds = stack.pop()
    if chain == 'A': accepted.append(conds)
    if chain in ['A','R']: continue

    negated_conds = []
    for r in wf[chain]:
        if len(r) == 2:
            stack.append((r[1], conds + [r[0]] + negated_conds))
            c = r[0].replace('<','>=') if '<' in r[0] else r[0].replace('>','<=')
            negated_conds.append(c)
        if len(r) == 1: stack.append((r[0], conds + negated_conds))

res = []
for r in accepted:
    ranges = {'x':[1,4000], 'm':[1,4000], 'a':[1,4000], 's':[1,4000]}
    for c in r:
        sign = c[1:3] if c[2] == '=' else c[1:2]
        match sign:
            case '<': ranges[c[0]][1] = min(ranges[c[0]][1], int(c[2:])-1)
            case '>': ranges[c[0]][0] = max(ranges[c[0]][0], int(c[2:])+1)
            case '<=': ranges[c[0]][1] = min(ranges[c[0]][1], int(c[3:]))
            case '>=': ranges[c[0]][0] = max(ranges[c[0]][0], int(c[3:]))
    res.append(math.prod([ rr[1]-rr[0]+1 for rr in ranges.values() ]))

print("Part 2:", sum(res))