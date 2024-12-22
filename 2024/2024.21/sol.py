import sys, pprint, collections, itertools, functools

data = '789\n456\n123\n 0A'
codepad = {complex(x, y): c for y, line in enumerate(data.split('\n'))
                            for x, c in enumerate(line.strip('\n'))}

data = ' ^A\n<v>'
ctrlpad = {complex(x, y): c for y, line in enumerate(data.split('\n'))
                            for x, c in enumerate(line.strip('\n'))}

codes = [s.strip() for s in open(sys.argv[1]) ]

@functools.cache
def shortest(gridtype, start, end):
    grid = codepad if gridtype == 0 else ctrlpad
    # BFS to calculate distances
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
        # print(f"pos: {pos}, path: {path}")
        if pos == start:
            paths.append(path[::-1])
            return
        for step in (1, -1, 1j, -1j):
            npos = pos + step
            if npos in seen and seen[npos] == seen[pos] - 1:
                dfs(npos, path + [-step])
        return

    dfs()
    return paths
    # pos, path = end, []
    # while pos != start:
    #     for step in (1, -1, 1j, -1j):
    #         npos = pos + step
    #         if npos in seen and seen[npos] == seen[pos] - 1:
    #             path.append(-step)
    #             pos = npos
    #             break
    # return path[::-1]

@functools.cache
def degree(s):
    return sum([1 for i in range(1,len(s)) if s[i] != s[i-1]])

MOVES = {1: '>', -1: '<', 1j: 'v', -1j: '^', 'A': 'A'}
ctrlpadhash = { '^':1, 'A':2, '<':1j, 'v':1+1j, '>':2+1j }

@functools.cache
def shortest2(start, end):
    p = shortest(1, start, end)
    rr = [''.join([MOVES[m] for m in opt]) for opt in p]
    deg = min([degree(a) for a in rr])
    return [[a for a in rr if degree(a) == deg][0]]

ans = 0
for code in codes:
    start, = [a for a in codepad if codepad[a] == 'A']
    res = []
    for i in range(len(code)):
        end, = [a for a in codepad if codepad[a] == code[i]]
        p = shortest(0, start, end)
        # print(f"Path from {codepad[start]}({start}) to {codepad[end]}({end}): {p}")

        rr = [''.join([MOVES[m] for m in opt]) for opt in p]
        res.append(rr)
        start = end

    # pprint.pp(res)

    # print(f"Stage 2")
    nopts = ['A'.join(s) + "A" for s in itertools.product(*res)]

    for i in range(int(sys.argv[2])):
        # print(f"Indirection {i+1}")

        opts, nopts = nopts, []
        # print(f"    Options: {len(opts)} {len(opts[0])} {opts}")

        cmdlen = None
        for cmd in opts:
            res = []
            start, = [a for a in ctrlpad if ctrlpad[a] == 'A']
            for j in range(len(cmd)):
                # end, = [a for a in ctrlpad if ctrlpad[a] == cmd[j]]
                end = ctrlpadhash[cmd[j]]
                res.append(shortest2(start, end))
                start = end

            t = ['A'.join(s) + "A" for s in itertools.product(*res)]
            # nopts.extend(t)
            # if cmdlen is None: cmdlen = len(t[0])
            # elif len(t[0]) < cmdlen: cmdlen = len(t[0])
            ncmdlen = len(t[0])
            if cmdlen is None:
                nopts = t
                cmdlen = ncmdlen
            elif ncmdlen < cmdlen:
                cmdlen = ncmdlen
                nopts = t
            elif ncmdlen == cmdlen:
                nopts.extend(t)


    print(f"{code}: {cmdlen}")
    ans += cmdlen * int(code.strip('A'))

print(ans)


