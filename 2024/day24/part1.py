import sys

state_lines, conn_lines = sys.stdin.read().strip().split('\n\n')

states = {}
for string in state_lines.split('\n'):
    name, val = string.split(':')
    states[name] = int(val)

conns = conn_lines.split('\n')
while conns:
    conn = conns.pop() 
    func, to = conn.split(' -> ')
    r1, op, r2 = func.split(' ')
    if r1 in states and r2 in states:
        if op == 'XOR':
            states[to] = states[r1] ^ states[r2]
        elif op == 'OR':
            states[to] = states[r1] | states[r2]
        elif op == 'AND':
            states[to] = states[r1] & states[r2]
    else:
        conns.insert(0, conn)

zs = []
for name, val in states.items():
    if name.startswith('z'):
        zs.append((name, val))

result = ''
for name, val in sorted(zs, reverse=True):
    result += str(val)

print(int(result, 2))
