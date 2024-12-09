#!/usr/bin/env python3

import sys, pprint, collections, copy

data = list(open(sys.argv[1]).read().strip())
disk, block, file_id = {}, 0, 0
file, free = collections.defaultdict(int), collections.defaultdict(int)
for i, c in enumerate(data):
    size = int(c)
    if i % 2 == 0:
        file[file_id] = (block, size)
        for j in range(block, block + size): disk[j] = file_id
        file_id, block = file_id + 1, block + size
    else:
        if size: free[block] = size
        for j in range(block, block + size): disk[j] = None
        block += size

o = copy.deepcopy(disk)

left, right = 0, len(disk) - 1
while left <= right:
    while disk[left] is not None and left <= right: left += 1
    if left >= right: break
    while left <= right and disk[right] is None: right -= 1
    if left >= right: break
    disk[left], disk[right] = disk[right], disk[left]

print("Part 1:", sum(i * c for i, c in disk.items() if c is not None))

def print_disk(disk):
    for k in disk:
        print(disk[k] if disk[k] is not None else '.', end='')
    print()

disk = o
for f in sorted(file, reverse=True):
    block, size = file[f]
    for tgt in sorted(free):
        if tgt >= block: break
        if free[tgt] < size: continue

        for i in range(size):
            disk[tgt + i], disk[block + i] = disk[block + i], None

        if free[tgt] > size: free[tgt+size] = free[tgt] - size
        del free[tgt]
        break

print("Part 2:", sum(i * c for i, c in disk.items() if c is not None))