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
count_dict = { element : 0 for element in elements }

n = 40

for j in range(n):
    new_states = { rule : 0 for rule in rules }
    for state, count in states.items():
        l = rules[state][0]
        r = rules[state][1]
        new_states[r] += count
        new_states[l] += count
        count_dict[l[1]] -= count
    states = new_states

for state, count in states.items():
    l, r = state
    count_dict[l] += count
    count_dict[r] += count

max_key = max(count_dict, key=count_dict.get)
min_key = min(count_dict, key=count_dict.get)

print(count_dict[max_key] - count_dict[min_key])
