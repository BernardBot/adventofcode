import sys

content = sys.stdin.read()
split = content.split("\n\n")
monkeys = []
for data in split:
    monkey = { 'inspect_count': 0 }
    for line in data.split("\n"):
        if 'Starting' in line:
            monkey['items'] = [int(x) for x in line.split(':')[1].split(',')]
        elif 'Operation' in line:
            monkey['operation'] = eval(f'lambda old: {line.split("=")[1]}')
        elif 'Test' in line:
            monkey['test'] = int(line.split('by')[1])
        elif 'If true' in line:
            monkey['true'] = int(line.split('monkey')[1])
        elif 'If false' in line:
            monkey['false'] = int(line.split('monkey')[1])
    monkeys.append(monkey)

mod = 1
for monkey in monkeys:
    mod *= monkey['test']

for _ in range(10000):
    for monkey in monkeys:
        while monkey['items']:
            item = monkey['items'].pop()
            monkey['inspect_count'] += 1
            value = monkey['operation'](item) % mod
            if value % monkey['test'] == 0:
                monkeys[monkey['true']]['items'].append(value)
            else:
                monkeys[monkey['false']]['items'].append(value)

s = sorted(m['inspect_count'] for m in monkeys)
print(s[-1] * s[-2])
