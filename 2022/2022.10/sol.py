#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as f: 
    data = [ l.strip() for l in f ]

ptr, reg = 0, 1
signal = [reg]
while len(signal) < 240:
    token = data[ptr].split()
    if token[0] == 'noop': signal.append(reg)
    else:
        signal.append(reg)
        reg += int(token[1])
        signal.append(reg)
    ptr += 1

res = sum(signal[i-1]*i for i in range(20,240,40))
print(f"Part 1: {res}")

for i in range(len(signal)):
    if i > 0 and i % 40 == 0: print()
    if abs(signal[i]-i%40) < 2: print('#',end='')
    else: print(' ',end='')
print()