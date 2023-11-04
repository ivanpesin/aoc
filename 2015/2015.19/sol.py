#!/usr/bin/env python3

import sys, pprint

with open(sys.argv[1]) as f:
    mapping, molecule = [ s.strip() for s in f.read().split('\n\n') ]
    rules, fold = {}, {}
    for r in mapping.split('\n'):
        s, t = r.split(' => ')
        fold[t] = s
        if s in rules:  rules[s].append(t)
        else:           rules[s] = [t]

    # pprint.pp(rules)
    results = set()
    for i in range(len(molecule)):
        for s in rules:
            if molecule[i:i+len(s)] == s:
                for t in rules[s]: results.add(molecule[:i] + t + molecule[i+len(s):])
    print(len(results))

    m, step = molecule, 0
    while m != 'e':
        for s in reversed(sorted(fold, key=lambda x: len(x))):
            if s in m:
                m = m.replace(s, fold[s], 1)
                step += 1
                break
    print(step)
