nums = list(map(int, open("inputa.txt").readlines()))

def check(n, ms):
    for m in ms:
        if n - m in ms:
            return True
    return False


s = 25
for i in range(s, len(nums)):
    n = nums[i]

    if check(n, set(nums[i-s:i])):
        continue
    
    print(n)
    break

