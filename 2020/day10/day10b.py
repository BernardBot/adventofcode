nums = set(map(int, open("inputb.txt").readlines()))

mem = [0] * (max(nums) + 1)
mem[0] = 1

for i in range(len(mem)):
    for j in [1,2,3]:
        if i + j in nums:
            mem[i + j] += mem[i]

print(mem[-1])
