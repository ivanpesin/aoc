import sys, re, json

data = open(sys.argv[1]).read()

print("Part 1:", sum(map(int, re.findall(r'-?\d+',data))))

def drop_red(obj):
    if "red" in obj.values(): return {}
    return obj

data2 = str(json.loads(data, object_hook=drop_red))
print("Part 2:", sum(map(int, re.findall(r'-?\d+',data2))))

