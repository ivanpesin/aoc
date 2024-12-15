#!/usr/bin/env python3

import sys, pprint, re, math, time, collections

data = open(sys.argv[1]).read()
grid = { complex(x, y): c for y, row in enumerate(data.split('\n\n')[0].split('\n'))
                          for x, c in enumerate(row) }
moves = ''.join(a.strip() for a in data.split('\n\n')[1])

STEP     = { '<': -1, '>': 1, '^': -1j, 'v': 1j }

robot_pos = [a for a in grid if grid[a] == '@'][0]

def draw(move=None):
    print(f"\033[H", end='', flush=True)
    max_x, max_y = int(max(a.real for a in grid)), int(max(a.imag for a in grid))
    for y in range(max_y+1):
        for x in range(max_x+1):
            if grid[complex(x, y)] == '@': print('\033[1;37m@\033[0m', end='')
            else:                          print(grid[complex(x,y)], end='')
        print()
    print(f"Pos: {robot_pos} Move: {move}    ")

print(f"\033[2J", end='', flush=True)
draw()
for move in moves:
    pos = robot_pos + STEP[move]
    while pos in grid and grid[pos] not in [ '.', '#' ]:
        pos += STEP[move]
    if pos in grid and grid[pos] == '.':
        while pos != robot_pos:
            grid[pos] = grid[pos-STEP[move]]
            pos += -STEP[move]
        grid[pos] = '.'
        robot_pos = pos = robot_pos + STEP[move]
    # draw(move)
    # time.sleep(0.1)

draw()
res = 0
for b in grid:
    if grid[b] == 'O':
        res += int(abs(b.real) + 100*abs(b.imag))
print(res)

grid2 = { complex(x, y): c for y, row in enumerate(data.split('\n\n')[0].split('\n'))
                          for x, c in enumerate(row) }
grid = {}
for a in grid2:
    x,y = int(a.real), int(a.imag)
    match grid2[a]:
        case '#': grid[complex(2*x,y)] = grid[complex(2*x+1,y)] = '#'
        case '.': grid[complex(2*x,y)] = grid[complex(2*x+1,y)] = '.'
        case '@': grid[complex(2*x,y)], grid[complex(2*x+1,y)] = '@', '.'
        case 'O': grid[complex(2*x,y)], grid[complex(2*x+1,y)] = '[', ']'

robot_pos = [a for a in grid if grid[a] == '@'][0]

print(f"\033[2J", end='', flush=True)
draw()
for move in moves:
    pos = robot_pos + STEP[move]
    if move in '<>':
        while pos in grid and grid[pos] not in [ '.', '#' ]:
            pos += STEP[move]
        if pos in grid and grid[pos] == '.':
            while pos != robot_pos:
                grid[pos] = grid[pos-STEP[move]]
                pos += -STEP[move]
            grid[pos] = '.'
            robot_pos = pos = robot_pos + STEP[move]
    else:
        start, visited, dir = [ robot_pos ], set([robot_pos]), STEP[move]
        blocked = False
        while start:
            p = start.pop()
            if grid[p+dir] == '[':
                start.extend([p+dir, p+dir+1])
                visited |= {p+dir, p+dir+1}
            elif grid[p+dir] == ']':
                start.extend([p+dir-1, p+dir])
                visited |= {p+dir-1, p+dir}
            elif grid[p+dir] == '#':
                blocked = True
                break
        if not blocked:
            for p in sorted(visited, key=lambda a: (a.imag, a.real), reverse=dir==1j):
                grid[p+dir], grid[p] = grid[p], grid[p+dir]
            robot_pos += STEP[move]

    # input()
    draw(move)
    time.sleep(0.05)

draw()

res = 0
for b in grid:
    if grid[b] == '[':
        res += int(abs(b.real) + 100*abs(b.imag))
print(res)
