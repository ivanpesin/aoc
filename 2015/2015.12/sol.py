#!/usr/bin/env python3

import sys, re

if __name__ == "__main__":

    with open(sys.argv[1]) as f:
        data = [ s.rstrip('\n') for s in f ]

    for obj in data:
        print("Part 1:", sum([ int(i) for i in re.findall(r'(-?\d+)', obj) ]))

        pos = -1
        while True:
            if (pos := obj.find('red', pos + 1)) < 0: break

            start = end = pos
            cutout = False
            list_level = dict_level = 0

            while start > 0:
                match obj[(start := start - 1)]:
                    case '}': dict_level += 1
                    case ']': list_level += 1
                    case '[':
                        list_level -= 1
                        if list_level < 0: break
                    case '{':
                        dict_level -= 1
                        if dict_level < 0:
                            cutout = True
                            break

            if cutout:
                dict_level = 0
                while not (obj[(end := end + 1)] == '}' and dict_level == 0):
                    if obj[end] == '{': dict_level += 1
                    elif obj[end] == '}': dict_level -= 1

                # print(f"cutout: {start}-{end} {obj[start:end+1]}")
                obj, pos = obj[:start] + obj[end+1:], start

        print("Part 2:", sum([ int(i) for i in re.findall(r'(-?\d+)', obj) ]) )
