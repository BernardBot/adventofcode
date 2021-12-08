lines = open("inputb.txt").readlines()

c = 0

ds = [2, 3, 4, 5, 5, 5, 6, 6, 6, 7]
ns = [1, 7, 4, 2, 3, 5, 0, 6, 9, 8]

for line in lines:
    fst, snd = line.split("|")

    fwords = fst.split()

    one, sev, four, two, thre, five, zero, six, nine, eight =\
        sorted(map(lambda s: "".join(sorted(s)), fwords), key=lambda s: len(s))

    xs = [two, thre, five]
    for x in xs:
        if len(set(x) & set(one)) == 2:
            thre = x
    xs.remove(thre)
    for x in xs:
        if len(set(x) & set(four)) == 3:
            five = x
        else:
            two = x
    
    ys = [zero, six, nine]

    for y in ys:
        if len(set(y) & set(sev)) == 2:
            six = y
    ys.remove(six)
    for y in ys:
        if len(set(y) & set(four)) == 4:
            nine = y
        else:
            zero = y

    d = {
        zero : "0",
        one : "1",
        two : "2",
        thre : "3",
        four : "4",
        five : "5",
        six : "6",
        sev : "7",
        eight : "8",
        nine : "9",
    }

    swords = snd.split()
    s = ""
    for sword in swords:
        s += d["".join(sorted(sword))]
    c += int(s)
print(c)