#!/usr/bin/env python3

import sys, pprint, hashlib

if __name__ == "__main__":

    with open(sys.argv[1]) as f:
        data = [ s.rstrip('\n') for s in f ]

    for s in data:
        i = 1
        while not hashlib.md5(bytes(s + str(i),'utf-8')).hexdigest().startswith('00000'): i+=1
        print("Part 1:", i)
        while not hashlib.md5(bytes(s + str(i),'utf-8')).hexdigest().startswith('000000'): i+=1
        print("Part 2:", i)
