#!/usr/bin/env python3

import sys, re

with open(sys.argv[1]) as f:
    data, moves = f.read().split('\n\n')

moves = re.findall(r"\d+|[LR]", moves)
pos, head = complex(data.splitlines()[0].index('.')), complex(1)
data = { complex(c,r):s for r,line in enumerate(data.splitlines()) for c,s in enumerate(line) }
W = int(sys.argv[2])

def jump(pos, head):
    x, y = pos.real, pos.imag
    sx, sy = x//W, y//W

    if W == 4: # test data jump matrix
        if   sy == 0 and head == -1: res = (complex(W+y,   W),              1j)
        elif sy == 0 and head ==  1: res = (complex(W*4-1, W*3-1-x),       -1)
        elif sy == 1 and head == -1: res = (complex(W*4-1-(y-W), W*3-1),   -1j)
        elif sy == 1 and head ==  1: res = (complex(W*4-1-(y-W), W*2),      1j)
        elif sy == 2 and head == -1: res = (complex(W*2-1-(y-2*W), W*2-1), -1j)
        elif sy == 2 and head ==  1: res = (complex(W*3-1, W-(y-W*3)),     -1)

        elif sx == 0 and head == -1j: res = (complex(W*3-1-x, 0),          1j)
        elif sx == 0 and head ==  1j: res = (complex(W*3-1-x,W*3-1),      -1j)
        elif sx == 1 and head == -1j: res = (complex(W*2, x-W),            1)
        elif sx == 1 and head ==  1j: res = (complex(W*2, W*3-1-(x-W)),    1)
        elif sx == 2 and head == -1j: res = (complex(W-1-(x-W*2),W),       1j)
        elif sx == 2 and head ==  1j: res = (complex(W-1-(x-W*2),W*2-1),  -1j)
        elif sx == 3 and head == -1j: res = (complex(W*3-1, W*2-(x-W*3)), -1)
        elif sx == 3 and head ==  1j: res = (complex(0, W*2-(x-W*3)),      1)

    if W == 50: # real input data jump matrix
        if   sy == 0 and head == -1: res = (complex(0, W*3-1-y),       1)  #
        elif sy == 0 and head ==  1: res = (complex(W*2-1, W*3-1-y),  -1)  #
        elif sy == 1 and head == -1: res = (complex(y-W, W*2),        1j)  #
        elif sy == 1 and head ==  1: res = (complex(W+y, W-1),       -1j)  #
        elif sy == 2 and head == -1: res = (complex(W, W*3-1-y),       1)  #
        elif sy == 2 and head ==  1: res = (complex(W*3-1,W*3-1-y),   -1)  #
        elif sy == 3 and head == -1: res = (complex(y-W*2,0),         1j)  #
        elif sy == 3 and head ==  1: res = (complex(y-W*2,W*3-1),    -1j)  #

        elif sx == 0 and head == -1j: res = (complex(W, W+x),         1)  #  
        elif sx == 0 and head ==  1j: res = (complex(W*2+x,0),        1j) #
        elif sx == 1 and head == -1j: res = (complex(0, W*2+x),       1)  #
        elif sx == 1 and head ==  1j: res = (complex(W-1,W*2+x),     -1)  #
        elif sx == 2 and head == -1j: res = (complex(x-W*2,W*4-1),   -1j) #
        elif sx == 2 and head ==  1j: res = (complex(W*2-1,x-W),     -1)  #

    return res

for move in moves:
    # print("Moving",pos,head,move)
    if   move == 'L': head *= -1j
    elif move == 'R': head *= +1j
    else: 
        for step in range(int(move)):
            npos, nhead = pos + head, head
            if npos not in data or data[npos] == ' ': npos, nhead = jump(npos,nhead)
            if data[npos] == '.': pos, head = npos, nhead

print("Part 2:",(pos.imag+1)*1000+(pos.real+1)*4+[1,1j,-1,-1j].index(head),pos)