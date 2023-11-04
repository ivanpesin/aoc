#!/usr/bin/env pypy3

import sys, pprint

if __name__ == "__main__":

    data = []
    with open(sys.argv[1]) as f:
        for s in f:
            words = s.strip('\n').split()
            if words[0] == 'turn': data.append( (words[1], *map(int,words[2].split(',')), *map(int,words[4].split(','))) )
            else:                  data.append( (words[0], *map(int,words[1].split(',')), *map(int,words[3].split(','))) )

    # pprint.pprint(data)

    lights = {}
    brightness = {}
    for x in range(1000):
        if x > 0 and x % 50 == 0: print("") 
        print(".", end='', flush=True)
        for y in range(1000):
            for d in data:
                if x >= d[1] and x <= d[3] and y >= d[2] and y <= d[4]:
                    if d[0] == 'on': 
                        lights[(x,y)] = 1
                        brightness[(x,y)] = brightness.get((x,y),0) + 1
                    elif d[0] == 'off': 
                        lights[(x,y)] = 0
                        brightness[(x,y)] = max(0, brightness.get((x,y),0) - 1)
                    elif d[0] == 'toggle': 
                        lights[(x,y)] = 1 - lights.get((x,y),0)
                        brightness[(x,y)] = brightness.get((x,y),0) + 2

    print("\nPart 1:", sum(lights.values()))
    print("Part 2:", sum(brightness.values()))