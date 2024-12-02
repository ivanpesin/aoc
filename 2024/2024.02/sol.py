import sys, pprint

data = [ list(map(int,s.split())) for s in open(sys.argv[1]).readlines() ]

def is_safe(a, part2=False):
    sign = 1 if a[1] - a[0] > 0 else -1
    for i in range(1, len(a)):
        if 0 < (sign * (a[i] - a[i-1])) < 4: pass
        elif part2: return any(is_safe(a[:i] + a[i+1:], False) for i in range(len(a)))
        else: return False
    return True

res1 = res2 = 0
for a in data:
    if is_safe(a): res1 +=1
    if is_safe(a, True): res2 +=1

print("Part 1:", res1)
print("Part 2:", res2)
# pprint.pp(data)