#!/usr/bin/env python3

import sys, collections, math

class Monkey():
    def __init__(self) -> None:
        self.items     = collections.deque()
        self.next      = {}
        self.worryfunc = lambda: None
        self.mod = self.inspections = 0

    def __repr__(self) -> str:
        return f"mod={self.mod:2d} inspections={self.inspections:3d} next={self.next}" # items={self.items}"

part = int(sys.argv[2])
monkeys, maxdiv = [], 1

for l in open(sys.argv[1]):
    match l.strip().split():
        case ["Monkey", i]: 
            i = int(i.strip(':'))
            monkeys.append(Monkey())
        case ["Starting", *rest]:
            monkeys[i].items = collections.deque(map(int,l.split(':')[1].split(',')))
        case ["Operation:", *rest]:
            monkeys[i].worryfunc = eval(f"lambda old: {l.split('= ')[1]}")
        case ["Test:", *rest]:
            monkeys[i].mod = int(l.split()[-1])
            maxdiv *= monkeys[i].mod
        case ["If", "true:", *rest]:  monkeys[i].next[1] = int(l.split()[-1])
        case ["If", "false:", *rest]: monkeys[i].next[0] = int(l.split()[-1])

for i in range(len(monkeys)):
    print(f"Monkey {i}: {monkeys[i]}")

rounds = 20 if part == 1 else 10_000
for r in range(rounds):
    print(f"Round {r}")
    for i,m in enumerate(monkeys):
        while m.items:
            m.inspections += 1
            item = m.items.popleft()
            if part == 1: item = m.worryfunc(item) // 3
            else        : item = m.worryfunc(item) #% maxdiv
            nm = m.next[item % m.mod == 0]
            monkeys[nm].items.append(item)

print(math.prod(sorted(m.inspections for m in monkeys)[-2:]))