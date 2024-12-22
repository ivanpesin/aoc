import sys, pprint, collections, tqdm

def next_secret(secret):
    secret = (secret ^   (secret * 64))  % 16777216
    secret = (secret ^  (secret // 32))  % 16777216
    secret = (secret ^ (secret * 2048))  % 16777216
    return secret

data = [ int(s) for s in open(sys.argv[1]) ]

res1, res2 = 0, collections.defaultdict(int)
for secret in tqdm.tqdm(data):
    trail, seen = collections.deque(maxlen=4), {}
    price = secret % 10
    for i in range(int(sys.argv[2])-1):
        secret = next_secret(secret)
        chg = (secret % 10) - price
        price = secret % 10
        trail.append(chg)
        if len(trail) == 4:
            if tuple(trail) not in seen:
                seen[tuple(trail)] = True
                res2[tuple(trail)] += price
    res1 += next_secret(secret)

print("Part 1:", res1)
print("Part 2:", max(res2.items(), key=lambda x: x[1])[1])