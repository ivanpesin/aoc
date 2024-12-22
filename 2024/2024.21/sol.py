import sys, pprint, collections, functools

data = '789\n456\n123\n 0A'
codepad = {complex(x, y): c for y, line in enumerate(data.split('\n'))
                            for x, c in enumerate(line.strip('\n'))}

data = ' ^A\n<v>'
ctrlpad = {complex(x, y): c for y, line in enumerate(data.split('\n'))
                            for x, c in enumerate(line.strip('\n'))}

codes = [s.strip() for s in open(sys.argv[1]) ]

MOVES = {1: '>', -1: '<', 1j: 'v', -1j: '^', 'A': 'A'}
codepad_start, = [a for a in codepad if codepad[a] == 'A']
ctrlpad_start, = [a for a in ctrlpad if ctrlpad[a] == 'A']

@functools.cache
def shortest(codepadgrid, start, end):
    grid = codepad if codepadgrid else ctrlpad

    q, seen = collections.deque([(0, start)]), {start: 0}
    while q:
        dist, pos = q.popleft()
        if end in seen and dist > seen[end]: break

        for step in (1, -1, 1j, -1j):
            npos = pos + step
            if npos in grid and npos not in seen and grid[npos] != ' ':
                seen[npos] = dist + 1
                q.append((dist + 1, npos))

    paths = []
    def dfs(pos=end, path=[]):
        if pos == start:
            paths.append(path[::-1])
            return
        for step in (1, -1, 1j, -1j):
            npos = pos + step
            if npos in seen and seen[npos] == seen[pos] - 1:
                dfs(npos, path + [-step])

    dfs() # all possible path steps
    return paths

@functools.cache
def seqlen(codepadgrid, seq, lvl, start):
    if not seq: return 0

    if codepadgrid: end, = [a for a in codepad if codepad[a] == seq[0]]
    else:           end, = [a for a in ctrlpad if ctrlpad[a] == seq[0]]

    paths = shortest(codepadgrid, start, end)

    if lvl == 0: mlen = len(paths[0])+1
    else:
        plen = []
        for p in paths:
            mpath = ''.join(MOVES[m] for m in p)
            plen.append(seqlen(False, mpath + 'A', lvl-1, ctrlpad_start))
        mlen = min(plen)

    return mlen + seqlen(codepadgrid, seq[1:], lvl, end)

res = 0
for code in codes:
    c = seqlen(True, code, int(sys.argv[2]), codepad_start)
    res += c * int(code[:-1])

print(res)