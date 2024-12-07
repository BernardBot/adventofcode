f = open("inputb.txt").read()

c = 0

for p in f.split("\n\n"):
    s = set("abcdefghijklmnopqrstuvwxyz")
    for l in p.splitlines():
        s &= set(l)
    c += len(s)

print(c)