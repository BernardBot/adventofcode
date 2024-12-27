import sys
regs, code = sys.stdin.read().strip().split('\n\n')
code = [int(x) for x in code.split(' ')[-1].split(',')]
# code = [
#     2, 4, # rb = ra % 8
#     1, 5, # rb = rb ^ 5
#     7, 5, # rc = ra // (2 ** rb) = ra >> rb
#     1, 6, # rb = rb ^ 6
#     0, 3, # ra = ra // (2 ** 3) = ra >> 3
#     4, 6, # rb = rb ^ rc
#     5, 5, # out.append(rb % 8)
#     3, 0, # jump to start if ra == 0
# ]

def simulate(ra):
    out = []

    ip = 0
    rb = 0
    rc = 0

    while ip < len(code):
        opcode = code[ip]
        literal = code[ip+1]
        if literal <= 3:
            combo = literal
        elif literal == 4:
            combo = ra
        elif literal == 5:
            combo = rb
        elif literal == 6:
            combo = rc

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

    return out

for i in range(0, 4096):
    out = simulate(i << 36)
    if out[12:16] == code[12:16]:
        for j in range(0, 4096):
            out = simulate((i << 36) + (j << 24))
            if out[8:16] == code[8:16]:
                for k in range(0, 4096):
                    out = simulate((i << 36) + (j << 24) + (k << 12))
                    if out[4:16] == code[4:16]:
                        for l in range(0, 4096):
                            out = simulate((i << 36) + (j << 24) + (k << 12) + l)
                            if out == code:
                                print((i << 36) + (j << 24) + (k << 12) + l)
                                exit()