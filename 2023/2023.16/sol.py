#!/usr/bin/env python3

import sys

data = { complex(c,r): ch for r,s in enumerate(open(sys.argv[1]).readlines())
                          for c,ch in enumerate(s.strip()) }
rows, cols = max(int(c.imag) for c in data)+1, max(int(c.real) for c in data)+1
inside = lambda pos: pos.imag in range(rows) and pos.real in range(cols)

def show(traces=False):
    for r in range(rows):
        for c in range(cols):
            if traces:
                if complex(c,r) in energized: print('#', end='')
                else: print(data[complex(c,r)], end='')
            else:
                print(data[complex(c,r)], end='')
        print()

def walk(data, stack, visited):
    while stack:
        pos, dir = stack.pop()
        if (pos, dir) in visited: continue
        visited[pos,dir] = True

        next = []
        if data[pos] == '.': next.append((pos+dir, dir))
        elif data[pos] == '/':
            if dir == 1:   next.append((pos-1j, -1j))
            if dir == -1:  next.append((pos+1j, 1j))
            if dir == 1j:  next.append((pos-1, -1))
            if dir == -1j: next.append((pos+1, 1))
        elif data[pos] == '\\':
            if dir == 1:   next.append((pos+1j, 1j))
            if dir == -1:  next.append((pos-1j, -1j))
            if dir == 1j:  next.append((pos+1, 1))
            if dir == -1j: next.append((pos-1, -1))
        elif data[pos] == '-':
            if (dir == 1 or dir == -1): next.append((pos+dir, dir))
            if dir == 1j or dir == -1j: next.extend([(pos+1, 1), (pos-1, -1)])
        elif data[pos] == '|':
            if (dir == 1j or dir == -1j): next.append((pos+dir, dir))
            if dir == 1 or dir == -1: next.extend([(pos+1j, 1j), (pos-1j, -1j)])
        for p,d in next:
            if inside(p) and (p,d) not in visited: stack.append((p,d))

def energized(start, direction):
    visited = {}
    walk(data.copy(), [ (start, direction) ], visited)
    return len(set(t[0] for t in visited))

print("Part 1:", energized(0,1))

energies = {}
for r in range(rows):
    energies[complex(0,r)] = energized(complex(0,r), 1)
    energies[complex(cols-1,r)] = energized(complex(cols-1,r), -1)

for c in range(cols):
    energies[complex(c,0)] = energized(complex(c,0), 1j)
    energies[complex(c,rows-1)] = energized(complex(c,rows-1), -1j)

print("Part 2:", max(energies.items(), key=lambda x: x[1]))