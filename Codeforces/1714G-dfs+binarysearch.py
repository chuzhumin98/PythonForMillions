###
# Solution:
# iteration version of DFS + Binary Search the prefix path sum of array B
# the worst complexity is O(n*logn), where n is the worst max tree depth
###

def binary_search(arr, target): # find the first to no more than target value
    low, high = 0, len(arr)-1
    while True:
        if high - low <= 0:
            if arr[low] > target:
                return low - 1
            else:
                return low
        middle = (low + high) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle] > target:
            high = middle - 1
        else:
            low = middle + 1

t = int(input())
for _ in range(t):
    n = int(input())
    edges = [[] for __ in range(n+1)]
    Rs = [0 for __ in range(n+1)]
    As = [0 for __ in range(n+1)]
    Bs = [0 for __ in range(n+1)]
    parents_list = [-1 for __ in range(n+1)]
    for child in range(n-1):
        arr = input().strip().split()
        parent, a, b = [int(i) for i  in arr]
        As[child + 2] = a
        Bs[child + 2] = b
        parents_list[child+2] = parent
        edges[parent].append(child + 2)

    stack = [1]
    prefixA_sum, prefixB_sums, path = 0, [0], []
    while True:
        if len(stack) == 0:
            break
        current_idx = stack.pop()

        if len(path) > 0:
            parent = parents_list[current_idx]
            while True:
                if path[-1] == parent:
                    break
                pop_idx = path.pop()
                prefixA_sum -= As[pop_idx]
                prefixB_sums.pop()

        prefixA_sum += As[current_idx]
        path.append(current_idx)
        value_new = prefixB_sums[-1] + Bs[current_idx]
        prefixB_sums.append(value_new)

        Rs[current_idx] = binary_search(prefixB_sums, prefixA_sum) - 1

        for edge in edges[current_idx]:
            stack.append(edge)


    print(' '.join([str(num) for num in Rs[2:]]))

