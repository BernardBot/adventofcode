nums = list(map(int, open("inputa.txt").readlines()))

def search(x, rmain, difs):
    if not rmain:
        return difs

    for a in [x+1,x+2,x+3]:
        if a in rmain:
            r = search(a, rmain - set([a]), difs + [a-x])

            if r is not None:
                return r

r = search(0, set(nums), [])
ones = r.count(1)
threes = r.count(3) + 1
print(ones * threes)