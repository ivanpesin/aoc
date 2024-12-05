import sys, pprint, collections

rule_str, update_str = open(sys.argv[1]).read().split('\n\n')
rules, update = {}, []

for r in rule_str.split('\n'):
    for left, right in [r.split('|')]:
        if right in rules: rules[right].append(left)
        else: rules[right] = [ left ]

def is_correct(a):
    for i in range(len(a)):
        if a[i] in rules:
            for b in rules[a[i]]:
                if b in a[i:]:
                    return False
    return True

def reorder(a):
    res = a[:]
    while not is_correct(res):
        for i in range(len(res)):
            if res[i] in rules:
                for b in rules[res[i]]:
                    if b in res[i:]:
                        res = res[:i] + [b] + res[i:res.index(b)] + res[res.index(b)+1:]
                        break
    return res

res = res2 = 0
for u in update_str.split('\n'):
    update, correct = u.split(','), True
    for i in range(len(update)):
        if not is_correct(update):
            correct = False
            break
    if correct: res  += int(update[len(update)//2])
    else:       res2 += int(reorder(update)[len(update)//2])

print("Part 1:", res)
print("Part 2:", res2)
