import sys

input = sys.stdin.read()
elfs = input.split("\n\n")
calorie_totals = []
for elf in elfs:
    calories = [int(x) for x in elf.split()]
    calorie_totals.append(sum(calories))
print(sum(sorted(calorie_totals)[-3:]))
