lines = open("inputa.txt").readlines()

c = 0
for line in lines:
    fst, snd = line.split("|")

    words = snd.split()
    for word in words:
        if len(word) in [2, 3, 4, 7]:
            c += 1

print(c)