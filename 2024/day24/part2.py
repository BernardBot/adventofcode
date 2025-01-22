import sys

state_lines, conn_lines = open('input').read().strip().split('\n\n')

g_states = {}
for string in state_lines.split('\n'):
    gate, val = string.split(':')
    g_states[gate] = 0 # we ignore the value

g_conns = []
for line in conn_lines.split('\n'):
    func, to = line.split(' -> ')
    r1, op, r2 = func.split(' ')
    g_conns.append((r1, op, r2, to))

def _simulate(states, conns):
    count = 0
    while conns:
        conn = conns.pop()
        r1, op, r2, to = conn
        if r1 in states and r2 in states:
            count = 0
            if op == 'XOR':
                states[to] = states[r1] ^ states[r2]
            elif op == 'OR':
                states[to] = states[r1] | states[r2]
            elif op == 'AND':
                states[to] = states[r1] & states[r2]
        else:
            count += 1
            conns.insert(0, conn)
            if count == len(conns):
                # Unable to simulate return impossible result
                return -1

    zs = []
    for name, val in states.items():
        if name.startswith('z'):
            zs.append((name, val))

    result = ''
    for name, val in sorted(zs, reverse=True):
        result += str(val)

    return int(result, 2)

def simulate(gates):
    states = dict(g_states)
    conns = list(g_conns)
    for gate in gates:
        states[gate] = 1
    return _simulate(states, conns)

def simulate_swapped(gates, i, j):
    states = dict(g_states)
    conns = list(g_conns)
    for gate in gates:
        states[gate] = 1
    r1, op, r2, to = conns[i]
    _r1, _op, _r2, _to = conns[j]
    conns[i] = r1, op, r2, _to
    conns[j] = _r1, _op, _r2, to
    return _simulate(states, conns)


def search(x):
    for i in range(len(g_conns)):
        for j in range(i + 1, len(g_conns)):
            r1, op, r2, to = g_conns[i]
            _r1, _op, _r2, _to = g_conns[j]

            if to.startswith('z'):
                if 'x' in _r1:
                    continue
                if _op != 'XOR':
                    continue
            
            if _to.startswith('z'):
                if 'x' in r1:
                    continue
                if op != 'XOR':
                    continue

            gate = 'x' + str(x - 1).zfill(2)
            result = simulate_swapped([gate], i, j)
            if result != 2 ** (x - 1):
                continue

            gate = 'x' + str(x).zfill(2)
            result = simulate_swapped([gate], i, j)
            if result != 2 ** x:
                continue

            gate = 'x' + str(x + 1).zfill(2)
            result = simulate_swapped([gate], i, j)
            if result != 2 ** (x + 1):
                continue
        
            gate1 = 'x' + str(x - 1).zfill(2)
            gate2 = 'y' + str(x - 1).zfill(2)
            result = simulate_swapped([gate1, gate2], i, j)
            if result != 2 ** x:
                continue

            gate1 = 'x' + str(x).zfill(2)
            gate2 = 'y' + str(x).zfill(2)
            result = simulate_swapped([gate1, gate2], i, j)
            if result != 2 ** (x + 1):
                continue
                
            gate1 = 'x' + str(x - 1).zfill(2)
            gate2 = 'y' + str(x - 1).zfill(2)
            gate3 = 'x' + str(x).zfill(2)
            result = simulate_swapped([gate1, gate2, gate3], i, j)
            if result != 2 ** (x + 1):
                continue

            return [to, _to]

outputs_swapped = []
for x in range(len(g_states) // 2):
    gate = 'x' + str(x).zfill(2)
    result = simulate([gate])
    if result != 2 ** x:
        outputs_swapped.extend(search(x))

# djg,dsd,hjm,mcq,sbg,z12,z19,z37
print(','.join(sorted(outputs_swapped)))
