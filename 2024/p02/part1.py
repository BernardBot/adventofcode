import sys

def is_safe(numbers):
    increasing = numbers[0] < numbers[1]
    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i - 1]
        if (
            (diff < 0 and increasing) or 
            (diff > 0 and not increasing) or 
            abs(diff) < 1 or 
            abs(diff) > 3
        ):
            return False
    return True

safe_count = 0
for line in sys.stdin.readlines():
    numbers = [int(item) for item in line.split()]
    safe_count += is_safe(numbers)

print(safe_count)

