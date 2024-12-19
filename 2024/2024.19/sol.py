import sys, pprint, functools

a, b = open(sys.argv[1]).read().split('\n\n')

patterns = a.split(', ')
designs  = b.split('\n')
maxl = max(len(p) for p in patterns)

@functools.lru_cache(maxsize=None)
def braid(d):
    res = 0
    for i in range(1, min(maxl,len(d))+1):
        if d[:i] in patterns:
            if d[i:] == '': res += 1
            else: res += braid(d[i:])
    return res

print("Part 1:", sum(1 for d in designs if braid(d)))
print("Part 2:", sum(braid(d) for d in designs))
