#!/usr/bin/env python3

import sys

data = [ [*map(int, s.split())] for s in open(sys.argv[1]) ]

def predict(seq):
    diffs = [ b-a for a, b in zip(seq, seq[1:]) ]
    return seq[-1] + (predict(diffs) if any(diffs) else 0)


print("Part 1:", sum(predict(seq) for seq in data))
print("Part 2:", sum(predict(seq[::-1]) for seq in data))