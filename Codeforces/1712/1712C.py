###
# Solution:
# consider from the completely zero condition, and relax value to non-zero from tail to head,
# until the array unsatisfy the non-decreasing constraints
###
t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().split()
    arr = [int(i) for i in arr]

    nums_set = set()
    nums_idxs = [[] for __ in range(n+1)]
    for i, num in enumerate(arr):
        nums_idxs[num].append(i)
        nums_set.add(num)

    idx = n - 1
    min_post = n + 1
    while True:
        if idx < 0:
            break
        if arr[idx] >= min_post:
            break
        min_post = arr[idx]
        if arr[idx] in nums_set:
            n_thisnum = len(nums_idxs[arr[idx]])
            if nums_idxs[arr[idx]][0] != idx - n_thisnum + 1:
                break
            nums_set.remove(arr[idx])
            idx -= n_thisnum
    print(len(nums_set))

