lines = open("inputa.txt").readlines()

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

print(a)