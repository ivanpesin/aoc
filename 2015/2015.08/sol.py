#!/usr/bin/env python3

import sys, re

if __name__ == "__main__":

    with open(sys.argv[1]) as f:
        data = [ s.strip() for s in f ]

    code = chars = encoded = 0
    for s in data:
        code += len(s)
        ss = re.sub(r'\\x[0-9a-f]{2}|\\"|\\\\', '_', s[1:-1])
        chars += len(ss)
        encoded += len(s.translate(str.maketrans({'"': '\\"', '\\': '\\\\',}))) + 2

    print(code, chars, encoded)

    print("Part 1:", code - chars)
    print("Part 2:", encoded - code)
