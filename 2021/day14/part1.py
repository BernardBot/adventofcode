lines = open("inputa.txt").readlines()

template = lines[0].strip()
rules = {}

for line in lines[2:]:
    fr, to = line.strip().split(" -> ")
    rules[fr] = to

n = 10
for _ in range(n):
    new_template = ""
    for i in range(len(template) - 1):
        sub = template[i:i+2]
        new_template += sub[0] + rules[sub]
    template = new_template + template[-1]

count_dict = { char : template.count(char) for char in set(template)}
max_key = max(count_dict, key=count_dict.get)
min_key = min(count_dict, key=count_dict.get)

print(count_dict[max_key] - count_dict[min_key])