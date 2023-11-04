#!/usr/bin/env python3

import sys, pprint

def is_valid(s: list):
    for ch in 'iol':
        if ch in s: return False
    
    dups = set()
    for i in range(1, len(s)):
        if s[i] == s[i-1]: dups.add(s[i])
    if len(dups) < 2: return False

    for i in range(len(s)-2):
        if ord(s[i]) == ord(s[i+1])-1 == ord(s[i+2])-2: break
    else:
        return False
    
    return True

def next_pwd(s: list):
    done = False
    while not done:
        for i in range(len(s)-1, -1, -1):
            if s[i] == 'z': s[i] = 'a'
            else:
                s[i] = chr(ord(s[i])+1)
                break
        if is_valid(s): done = True
    return s

print(f"Valid password: {is_valid(list(sys.argv[1]))}")
print(f"Next password is: {''.join(next_pwd(list(sys.argv[1])))}")