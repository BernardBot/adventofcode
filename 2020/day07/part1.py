lines = open("inputa.txt").readlines()

d = dict()

for line in lines:
    key, values = line.split("contain")
    key = key.split("bag")[0].strip()
    values = set(map(lambda bag: " ".join(bag.split(" ")[2:4]), values.split(",")))
    d[key] = values

gold = "shiny gold"

def find_bag(bag, s):
    if bag not in d:
        return False
    values = d[bag]
    if gold in values:
        return True
    if values <= s:
        return False
    s = s | values
    for value in values:
        if find_bag(value, s):
            return True

    return False

print(sum(find_bag(bag, set([bag])) for bag in d))