#!/usr/bin/env python3

import sys
import re
import json

with open(sys.argv[1]) as f:
    data = f.read()

print(sum(map(int, re.findall(r'-?\d+',data))))

balance = json.loads(data)

#balance = json.loads(r'{"a": [1,"red",5]}')
def walk(d):
    if isinstance(d,dict):
        for k in d:
            if isinstance(d[k],str) and d[k] == 'red': return False
        rm = set()
        for k in d:
            if isinstance(d[k],dict):
                if not walk(d[k]): rm.add(k)
            elif isinstance(d[k],list):
                d[k] = walk(d[k])
        for k in rm: del d[k]
        return True
    elif isinstance(d,list):
        tmp = []
        for i in d:
            if isinstance(i,dict):
                if walk(i): tmp.append(i)
            elif isinstance(i,list):
                tmp.append(walk(i))
            else:
                tmp.append(i)
        return tmp
    else: raise RuntimeError

walk(balance)

print(sum(map(int, re.findall(r'-?\d+',json.dumps(balance)))))