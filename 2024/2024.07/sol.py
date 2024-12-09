import sys, pprint
import itertools

data = []
for s in open(sys.argv[1]):
    left, right = s.strip().split(': ')
    right = right.split()
    data.append((int(left), [int(x) for x in right]))

def solve(part2=0):
    res = 0
    for test, nums in data:
        ops = '+*|' if part2 else '+*'
        for combination in itertools.product(ops, repeat=(len(nums)-1)):
            r = nums[0]
            for i, op in enumerate(combination):
                if op == '+': r += nums[i+1]
                if op == '*': r *= nums[i+1]
                if op == '|': r = int(str(r) + str(nums[i+1]))

            if r == test:
                res += test
                break
    return res


print("Part 1:", solve())
print("Part 2:", solve(1))