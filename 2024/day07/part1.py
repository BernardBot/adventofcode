import sys

score = 0
for line in sys.stdin.readlines():
    target, values = line.split(":")
    target = int(target)
    values = [int(val) for val in values.split()]
    results = [values[0]]
    for val in values[1:]:
        new_results = []
        for result in results:
            new_results.append(result + val)
            new_results.append(result * val)
        results = new_results

    for result in results:
        if result == target:
            score += result
            break

print(score)