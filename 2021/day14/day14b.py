lines = open("inputb.txt").readlines()

template = lines[0].strip()

rules = {}
for line in lines[2:]:
    fr, to = line.strip().split(" -> ")
    rules[fr] = [fr[0] + to, to + fr[1]]

states = { rule : 0 for rule in rules }
for i in range(len(template) - 1):
    sub = template[i:i+2]
    states[sub] += 1

elements = set("".join(rules))
overlap = { element : 0 for element in elements }

n = 40

for j in range(n):
    new_states = { rule : 0 for rule in rules }
    for state, count in states.items():
        l = rules[state][0]
        r = rules[state][1]
        new_states[r] += count
        new_states[l] += count
        overlap[l[1]] += count
    states = new_states

count_dict = {}

for state, count in states.items():
    l, r = state
    if l in count_dict:
        count_dict[l] += count
    else:
        count_dict[l] = count
    if r in count_dict:
        count_dict[r] += count
    else:
        count_dict[r] = count

for element, count in overlap.items():
    count_dict[element] -= count

max_key = max(count_dict, key=count_dict.get)
min_key = min(count_dict, key=count_dict.get)

print(count_dict[max_key] - count_dict[min_key])