import sys

numbers = [int(x) for x in sys.stdin.read().split()]

for _ in range(25):
    new_numbers = []
    for n in numbers:
        if n == 0:
            new_numbers.append(1)
        elif len(str(n)) % 2 == 0:
            new_numbers.append(int(str(n)[:len(str(n)) // 2]))
            new_numbers.append(int(str(n)[len(str(n)) // 2:]))
        else:
            new_numbers.append(n * 2024)
    numbers = new_numbers
print(len(numbers))
