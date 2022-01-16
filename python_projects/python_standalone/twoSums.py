def twoSum(nums, target):
    l = []
    d = dict()
    for i, n in enumerate(nums):
        if target-n in d:
            l.append(d[target-n])
            l.append(i)
            break
        d[n] = i
    print(l)
    return l

twoSum([4,7,10,15], 11)