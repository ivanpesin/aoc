import sys, re, pprint

data = [ list(map(int,re.findall(r'\d+', s))) for s in open(sys.argv[1]).readlines() ]
left, right = sorted(a[0] for a in data), sorted(a[1] for a in data)
dist  = sum(abs(left[i] - right[i]) for i in range(len(left)))
score = sum(v * right.count(v) for v in left)

print("Part 1:", dist)
print("Part 2:", score)