import sys, pprint, re

data = open(sys.argv[1]).read().replace("\n", "")

def solve(part2):
    do, res = True, 0
    for instr in re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", data):
        if instr == "do()":
            do = True
        elif instr == "don't()":
            do = False
        elif not part2 or (part2 and do):
            a, b = map(int, re.findall(r'\d+', instr))
            res += a * b

    return res

print("Part 1:", solve(False))
print("Part 2:", solve(True))
