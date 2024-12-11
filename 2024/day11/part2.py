import collections
import sys

numbers = {int(x): 1 for x in sys.stdin.read().split()}

for _ in range(75):
    new_numbers = collections.defaultdict(int)
    for n, count in numbers.items():
        if n == 0:
            new_numbers[1] += count
        elif len(str(n)) % 2 == 0:
            new_numbers[int(str(n)[:len(str(n)) // 2])] += count
            new_numbers[int(str(n)[len(str(n)) // 2:])] += count
        else:
            new_numbers[n * 2024] += count
    numbers = new_numbers
print(sum(numbers.values()))
