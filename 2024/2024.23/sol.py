import sys, collections, pprint

conn = collections.defaultdict(set)
for s in open(sys.argv[1]):
    a,b = s.strip().split('-')
    conn[a].add(b); conn[b].add(a)

triangles = set()
for v in conn:
    for w in conn[v]:
        if w == v: continue
        for u in conn[w]:
            if not any(a[0] == 't' for a in (v,w,u)): continue
            if u == w: continue
            if v in conn[u]: triangles.add(tuple(sorted([v,w,u])))

print("Part 1:", len(triangles))

cliques = []
def maxclique(r, p, x):
    if not p and not x:
        if len(r) > 2: cliques.append(sorted(r))
        return

    for v in p.copy():
        maxclique(r | {v}, p & conn[v], x & conn[v])
        p.remove(v); x.add(v)

maxclique(set(), set(conn.keys()), set())
print("Part 2:", ','.join(max(cliques, key=len)))