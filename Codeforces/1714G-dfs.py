###
# Solution:
# iteration version of DFS, but TLE at test example 3, no need to say more about algorithm
# now we discuss about why DFS would TLE, here construct an example
# 1
# 20000
# 1 1 10000
# 2 1 1
# 3 1 1
# 4 1 1
# ...
# ...
# 9999 1 1
# 10000 10000 1
# 10001 1 10000
# 10002 10000 1
# 10003 1 10000
# ...
# ...
# 19998 10000 1
# 19999 1 10000
# we can find that in this test example, the calculation complexity is 10^10 for DFS
###

t = int(input())
for _ in range(t):
    n = int(input())
    edges = [[] for __ in range(n + 1)]
    Rs = [0 for __ in range(n + 1)]
    As = [0 for __ in range(n + 1)]
    Bs = [0 for __ in range(n + 1)]
    parents_list = [-1 for __ in range(n + 1)]
    for child in range(n - 1):
        arr = input().strip().split()
        parent, a, b = [int(i) for i in arr]
        As[child + 2] = a
        Bs[child + 2] = b
        parents_list[child + 2] = parent
        edges[parent].append(child + 2)

    stack = [1]
    prefixA_sum, prefixB_sum, prefixB_idx, path = 0, 0, -1, []
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
                if prefixB_idx == len(path):
                    prefixB_idx -= 1
                    prefixB_sum -= Bs[pop_idx]

            while True:
                if prefixB_sum <= prefixA_sum:
                    break
                prefixB_sum -= Bs[path[prefixB_idx]]
                prefixB_idx -= 1

        prefixA_sum += As[current_idx]
        path.append(current_idx)
        while True:
            if prefixB_sum + Bs[path[prefixB_idx + 1]] <= prefixA_sum:
                prefixB_sum += Bs[path[prefixB_idx + 1]]
                prefixB_idx += 1
            else:
                break

            if prefixB_idx >= len(path) - 1:
                break

        Rs[current_idx] = prefixB_idx

        for edge in edges[current_idx]:
            stack.append(edge)

    print(' '.join([str(num) for num in Rs[2:]]))