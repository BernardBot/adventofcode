lines = open("inputb.txt").readlines()

score = { ")" : 1, "]" : 2, "}" : 3, ">" : 4, }

o2c = dict(zip("([{<", ")]}>"))
c2o = dict(zip(")]}>", "([{<"))

cs = []

for line in lines:
    stack = []
    corrupted = False
    for c in line:
        if c in o2c:
            stack.append(c)
        elif c in c2o:
            if len(stack) == 0 or c2o[c] != stack[-1]:
                corrupted = True
                break
            stack.pop()

    if not corrupted:
        t = 0
        for c in reversed(stack):
            t = t * 5 + score[o2c[c]]
        cs.append(t)

print(sorted(cs)[len(cs) // 2])

