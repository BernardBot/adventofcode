import sys

digit_words = [
    'zero', 'one', 'two', 'three', 'four',
    'five', 'six', 'seven', 'eight', 'nine'
]
digits = list('0123456789')

score = 0
for line in sys.stdin.readlines():
    first = None
    line = line.strip()
    for i in range(len(line)):
        for j, digit_word in enumerate(digit_words):
            if line.startswith(digit_word, i):
                if first is None:
                    first = j
                last = j
        for j, digit in enumerate(digits):
            if line.startswith(digit, i):
                if first is None:
                    first = j
                last = j
    score += int(str(first) + str(last))
print(score)
