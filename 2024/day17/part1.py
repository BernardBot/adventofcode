import sys

regs, code = sys.stdin.read().strip().split('\n\n')

ra, rb, rc = regs.split('\n')
ra = int(ra.split(':')[-1])
rb = int(rb.split(':')[-1])
rc = int(rc.split(':')[-1])

code = [int(x) for x in code.split(' ')[-1].split(',')]

def get_combo(literal):
    if literal <= 3:
        return literal
    if literal == 4:
        return ra
    if literal == 5:
        return rb
    if literal == 6:
        return rc

ip = 0
out = []
while ip < len(code):
    opcode = code[ip]
    literal = code[ip+1]
    combo = get_combo(literal)
    if opcode == 0:
        ra = int(ra / 2 ** combo)
    elif opcode == 1:
        rb = rb ^ literal
    elif opcode == 2:
        rb = combo % 8
    elif opcode == 3:
        if ra != 0:
            ip = literal
            continue
    elif opcode == 4:
        rb = rb ^ rc
    elif opcode == 5:
        out.append(combo % 8)
    elif opcode == 6:
        rb = int(ra / 2 ** combo)
    elif opcode == 7:
        rc = int(ra / 2 ** combo)
    ip += 2
print(','.join([str(x) for x in out]))