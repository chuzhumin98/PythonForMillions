# Solution:
# to hold the property of non-decreasing order, you can only un-mask the array from the right to left.
# thus, we can first mask all the number to 0, then from right to left, one by one unmask the array,
# once the property non-decreasing is broken, then end the process, output the max unmask number (together with the min operation number)
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

