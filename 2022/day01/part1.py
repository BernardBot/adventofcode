import sys

input = sys.stdin.read()
elfs = input.split("\n\n")
max_calories = 0
for elf in elfs:
    calories = [int(x) for x in elf.split()]
    max_calories = max(sum(calories), max_calories)
print(max_calories)