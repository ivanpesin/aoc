import sys, pprint

locks, keys = [], []
for shape in open(sys.argv[1]).read().split('\n\n'):
    a, res = shape.splitlines(), []
    if a[0][0] == '#':
        for col in range(len(a[0])):
            res.append(max(row for row in range(len(a)) if a[row][col] == '#'))
        locks.append(res)
    else:
        for col in range(len(a[0])):
            res.append(len(a)-1- min(row for row in range(len(a)) if a[row][col] == '#'))
        keys.append(res)

fit = 0
for lock in locks:
    for key in keys:
        fit += all([ k+l < len(a)-1 for k,l in zip(key, lock) ])

print(fit)