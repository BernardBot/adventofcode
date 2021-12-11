lines = open("inputa.txt").readlines()

score = { "(" : 3, "[" : 57, "{" : 1197, "<" : 25137 }

o2c = dict(zip("([{<", ")]}>"))
c2o = dict(zip(")]}>", "([{<"))

bracks = []

for line in lines:
    stack = []
    for c in line:
        if c in o2c:
            stack.append(c)
        elif c in c2o:
            if len(stack) == 0 or c2o[c] != stack[-1]:
                bracks.append(c)
                break
            stack.pop()

c = 0
for brack in bracks:
    c += score[c2o[brack]]
print(c)