#!/usr/bin/env python3

import sys

data = { complex(c,r): ch for r,s in enumerate(open(sys.argv[1]).readlines())
                          for c,ch in enumerate(s.strip()) }
rows, cols = max(int(c.imag) for c in data)+1, max(int(c.real) for c in data)+1

def energy(todo):
    done = set()
    while todo:
        pos, dir = todo.pop()
        if data.get(pos) == None or (pos, dir) in done: continue
        done.add((pos, dir))

        match data[pos]:
            case '.': todo.append((pos+dir, dir))
            case '/':
                d = -complex(dir.imag, dir.real)
                todo.append((pos+d, d))
            case '\\':
                d = complex(dir.imag, dir.real)
                todo.append((pos+d, d))
            case '-':
                if not dir.imag: todo.append((pos+dir, dir))
                else: todo.extend([(pos+1, 1), (pos-1, -1)])
            case '|':
                if dir.imag: todo.append((pos+dir, dir))
                else: todo.extend([(pos+1j, 1j), (pos-1j, -1j)])

    return len(set(c[0] for c in done))

print("Part 1:", energy([ (0,1) ]))

energies = {}
for r in range(rows):
    energies[complex(0,r)] = energy([ (complex(0,r), 1) ])
    energies[complex(cols-1,r)] = energy([ (complex(cols-1,r), -1) ])

for c in range(cols):
    energies[complex(c,0)] = energy([ (complex(c,0), 1j) ])
    energies[complex(c,rows-1)] = energy([ (complex(c,rows-1), -1j) ])

print("Part 2:", max(energies.items(), key=lambda x: x[1]))