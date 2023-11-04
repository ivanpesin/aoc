#!/usr/bin/env pypy3

import sys, pprint

def solve(wires):
    while 'a' not in wires:
        for s in data:
            left, right = s.split(' -> ')
            if right in wires: continue

            words = left.split()
            if len(words) == 1: 
                if left.isdigit():  wires[right] = int(left)
                elif left in wires: wires[right] = wires[left]
            elif len(words) == 2:
                if "NOT" in left and words[1] in wires: 
                    wires[right] = ~wires[words[1]] & 0xffff
            else:
                if words[0].isdigit():  a = int(words[0]) 
                elif words[0] in wires: a = wires[words[0]]
                else: continue

                if words[2].isdigit():  b = int(words[2]) 
                elif words[2] in wires: b = wires[words[2]]
                else: continue

                if   "AND" in left:     wires[right] = a & b
                elif  "OR" in left:     wires[right] = a | b
                elif "LSHIFT" in left:  wires[right] = a << int(b)
                elif "RSHIFT" in left:  wires[right] = a >> int(b)

    return wires['a']

if __name__ == "__main__":

    with open(sys.argv[1]) as f:
        data = [ s.rstrip('\n') for s in f ]

    print("Part 1:", res := solve({}))
    print("Part 2:", solve({'b': res}))    