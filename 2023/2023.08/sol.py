#!/usr/bin/env python3

import sys, itertools, pprint, re, math

instr, rules = open(sys.argv[1]).read().split('\n\n')

nodes = {}
for s in rules.split('\n'):
    a = re.findall(r'[1-9A-Z]{3}',s)
    nodes[a[0]] = a[1:]

def part1():
    cnt, st = 0, 'AAA'
    for step in itertools.cycle(instr):
        st = nodes[st][0] if step == 'L' else nodes[st][1]
        cnt += 1
        if st == 'ZZZ': return cnt
    return None

def part2():
    cnt, start, clen = 0, [ n for n in nodes if n.endswith('A') ], []
    print(f"Start nodes: {start}")
    for st in start:
        seen = [(st,0)]
        for step in itertools.cycle(instr):
            n = nodes[st][0] if step == 'L' else nodes[st][1]
            cnt += 1

            instr_pos = cnt % len(instr)
            step_id = (n,instr_pos)
            if step_id in seen:
                pos = seen.index(step_id)
                print(f"Step {cnt}: {step_id}, cycle start pos {pos}, cycle len {len(seen) - pos}")
                clen.append(len(seen) - pos)
                break
            seen.append(step_id)
            st = n

    return math.lcm(*clen) if clen else None

print("Part 1:", part1())
print("Part 2:", part2())
