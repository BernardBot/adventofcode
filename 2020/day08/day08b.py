lines = open("inputb.txt").readlines()

def check():
    i = 0
    a = 0
    s = set()
    while i not in s:
        s.add(i)
        op = lines[i]

        if "nop" in op:
            i += 1
        elif "acc" in op:
            a += int(op.split()[-1])
            i += 1
        elif "jmp" in op:
            i += int(op.split()[-1])

        if i >= len(lines):
            return a


for j in range(len(lines)):
    op = lines[j]

    if "jmp" in op:
        lines[j] = lines[j].replace("jmp", "nop")
    elif "nop" in op:
        lines[j] = lines[j].replace("nop", "jmp")
    else:
        continue
    
    a = check()
    if a is not None:
        print(a)
        break
    lines[j] = op