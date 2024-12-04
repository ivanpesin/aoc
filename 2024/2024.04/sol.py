import sys, pprint, collections

data = [ s.strip() for s in open(sys.argv[1]).readlines() ]

res = 0
for row, s in enumerate(data):
    for col, c in enumerate(s):
        if c == "X":
            if col+4 <= len(s) and s[col:col+4] == "XMAS": res += 1
            if col-3 >= 0 and s[col-3:col+1] == "SAMX":    res += 1
            if row-3 >= 0 and ''.join(data[row-i][col] for i in range(4)) == "XMAS":         res += 1
            if row+4 <= len(data) and ''.join(data[row+i][col] for i in range(4)) == "XMAS": res += 1
            if (row-3 >= 0 and col-3 >= 0 and
                ''.join(data[row-i][col-i] for i in range(4)) == "XMAS"): res += 1
            if (row+4 <= len(data) and col+4 <= len(s) and
                ''.join(data[row+i][col+i] for i in range(4)) == "XMAS"): res += 1
            if (row-3 >= 0 and col+4 <= len(s) and
                ''.join(data[row-i][col+i] for i in range(4)) == "XMAS"): res += 1
            if (row+4 <= len(data) and col-3 >= 0 and
                ''.join(data[row+i][col-i] for i in range(4)) == "XMAS"): res += 1

print("Part 1:", res)

res = collections.defaultdict(int)
for row, s in enumerate(data):
    for col, c in enumerate(s):
        if c == "A":
            if (row-1 >= 0 and row+2 <= len(data) and
                col-1 >= 0 and col+2 <= len(s) and
                ''.join(data[row+i][col-i] for i in range(-1,2)) in ["SAM","MAS"]): res[row,col] += 1
            if (row-1 >= 0 and row+2 <= len(data) and
                col-1 >= 0 and col+2 <= len(s) and
                ''.join(data[row+i][col+i] for i in range(-1,2)) in ["SAM","MAS"]): res[row,col] += 1

print("Part 2:", sum( 1 for v in res.values() if v == 2 ))