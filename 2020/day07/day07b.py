lines = open("inputb.txt").readlines()

d = dict()

for line in lines:
    key, values = line.split("contain")
    key = key.split("bag")[0].strip()
    values = list(map(lambda bag: (" ".join(bag.split(" ")[2:4]), bag.split(" ")[1]), values.split(",")))
    d[key] = values

gold = "shiny gold"

def find_bag(bag):
    c = 1
    for value, weight in d[bag]:
        if value not in d:
            continue
        c += int(weight) * find_bag(value)
    return c

print(find_bag(gold) - 1)