nums = list(map(int, open("inputb.txt").readlines()))

n = 1639024365
i = 0
j = 0
s = 0

while s != n:
    if s < n:
        s += nums[i]
        i += 1
    else:
        s = nums[j]
        j += 1
        i = j
print(min(nums[j-1:i]) + max(nums[j-1:i]))
