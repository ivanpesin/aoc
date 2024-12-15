#!/usr/bin/env python3

import sys

data = open(sys.argv[1]).read()
grid = { complex(x, y): c for y, row in enumerate(data.split('\n\n')[0].split('\n'))
                          for x, c in enumerate(row) }
moves = ''.join(a.strip() for a in data.split('\n\n')[1])

STEP     = { '<': -1, '>': 1, '^': -1j, 'v': 1j }

def bfs(robot_pos, dir):
    start, visited, blocked = [ robot_pos ], set([robot_pos]), False
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
    return blocked, visited

def execute(part2):
    robot_pos = [a for a in grid if grid[a] == '@'][0]
    for move in moves:
        dir = STEP[move]
        pos = robot_pos + dir
        if not part2 or move in '<>':
            while pos in grid and grid[pos] not in [ '.', '#' ]:
                pos += dir
            if pos in grid and grid[pos] == '.':
                while pos != robot_pos:
                    grid[pos], pos = grid[pos-dir], pos-dir
                grid[pos] = '.'
                robot_pos += dir
        else:
            blocked, shape = bfs(robot_pos, dir)
            if blocked: continue
            for p in sorted(shape, key=lambda a: (a.imag, a.real), reverse=dir==1j):
                grid[p+dir], grid[p] = grid[p], grid[p+dir]
            robot_pos += dir

def grid_p2():
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

    return grid

for part2 in range(2):
    if part2: grid = grid_p2()
    execute(part2)
    res = int(sum(b.real + 100*b.imag for b in grid if grid[b] in '[O'))
    print(f"Part {part2+1}: {res}")