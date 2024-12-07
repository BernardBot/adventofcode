import sys

score = 0
for line in sys.stdin.readlines():
    opp, you = line.split()
    if opp == "A":
        if you == "X":
            score += 0 + 3
        elif you == "Y":
            score += 3 + 1
        elif you == "Z":
            score += 6 + 2
    elif opp == "B":
        if you == "X":
            score += 0 + 1
        elif you == "Y":
            score += 3 + 2
        elif you == "Z":
            score += 6 + 3
    elif opp == "C":
        if you == "X":
            score += 0 + 2
        elif you == "Y":
            score += 3 + 3
        elif you == "Z":
            score += 6 + 1
print(score)