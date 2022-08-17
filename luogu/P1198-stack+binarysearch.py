###
# Solution: monotonic stack + binary search, but TLE with python
# we can hold a monotonic decreasing stack to store the max value from each position to final.
# then we just need to binary search for the given index len(A) - L, the first no less than this index in the stack
# store the largest value from len(A)-L to the end of A
###

def binary_search(stack, num):
    low, high = 0, len(stack) - 1
    while True:
        if low >= high:
            if stack[low][1] >= num:
                return low
            else:
                return low + 1

        mid = (low + high) >> 1
        if stack[mid][1] < num:
            low = mid + 1
        elif stack[mid][1] > num:
            high = mid - 1
        else:
            return mid

M, D = input().split()
M, D = int(M), int(D)

stack = []
idx_now = 0
t = 0
for _ in range(M):
    oper, n = input().split()
    n = int(n)
    if oper == 'A':
        val = (n + t) % D
        while True:
            if len(stack) == 0:
                break
            if stack[-1][0] > val:
                break
            stack.pop()
        stack.append([val, idx_now])
        idx_now += 1
    else:
        idx_use = binary_search(stack, idx_now-n)
        print(stack[idx_use][0])
        t = stack[idx_use][0]