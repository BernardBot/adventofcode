lines = open("inputb.txt").read().strip().split("\n\n")

def wins(bingo, ns):
    for i in range(5):
        if set(bingo[i]) <= ns:
            return True
        if set([row[i] for row in bingo]) <= ns:
            return True
    return False

ns = list(map(int, lines[0].split(",")))
cards = []
for line in lines[1:]:
    l = line.split("\n")
    k = []
    for r in l:
        k.append([int(x) for x in r.strip().split()])
    cards.append(k)

ps = []
for n in ns:
    ps.append(n)
    
    new_cards = []
    for card in cards:
        if not wins(card, set(ps)):
            new_cards.append(card)

    if len(new_cards) == 0:
        card = cards[0]
        a = set()
        for row in card:
            a |= set(row)
        s = 0
        for x in a - set(ps):
            s += x
        print(s * n)
        exit()

    cards = new_cards
    