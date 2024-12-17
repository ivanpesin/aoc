import sys, re, copy
import pprint

state, program = open(sys.argv[1]).read().split('\n\n')

reg  = { chr(i+65): int(v) for i,v in enumerate(re.findall(r'\d+', state)) }
code = [ int(n) for n in re.findall(r'\d+', program) ]

def combo(reg, o):
    assert o < 7
    if o in range(4): return o
    if o in range(4, 7): return reg[chr(o+61)]

def run(reg):
    ptr, out = 0, []
    while ptr < len(code):
        op, operand = code[ptr], code[ptr+1]
        # print(f"ptr: {ptr} op: {op}, operand: {operand}")
        match op:
            case 0: reg['A'] = reg['A'] // 2**combo(reg, operand)
            case 1: reg['B'] ^= operand
            case 2: reg['B'] = combo(reg, operand) % 8
            case 3:
                if reg['A'] != 0:
                    ptr = operand
                    continue
            case 4: reg['B'] ^= reg['C']
            case 5: out.append(combo(reg, operand) % 8)
            case 6: reg['B'] = reg['A'] // 2**combo(reg, operand)
            case 7: reg['C'] = reg['A'] // 2**combo(reg, operand)
        ptr += 2
    return out


print("Part 1:", ','.join(map(str,run(reg))))

res, l = 0, len(code)-1
for i in range(l-2,-1,-1):
    j = res * 8
    while True:
        b = run({'A': j, 'B': 0, 'C': 0})
        if code[i:] == b:
            res = j
            break
        j += 1

print("Part 2:", res)