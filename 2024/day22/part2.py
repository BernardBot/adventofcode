import sys

master = {}

for line in sys.stdin.read().strip().split('\n'):
    value = int(line)
    values = [value]
    for _ in range(2000):
        value = ((value * 64) ^ value) % 16777216
        value = ((value // 32) ^ value) % 16777216
        value = ((value * 2048) ^ value) % 16777216
        values.append(value)

    prices = [x % 10 for x in values]

    dprices = []
    for i in range(len(prices) - 1):
        dprices.append(prices[i + 1] - prices[i])

    seen = set()
    for i in range(len(dprices) - 3):
        four = tuple(dprices[i: i + 4])
        if four not in seen:
            seen.add(four)
            price = prices[i + 4]
            if four in master:
                master[four] += price
            else:
                master[four] = price

best_total = max(master.values())
print(best_total)
