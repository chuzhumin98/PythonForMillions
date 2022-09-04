###
# Solution: priority queue + greedy
# note that every node can undertake most is just all the remaining linked to it, so we hold with a pq,
# each time we remove the min value of linked weight sum of each vertex, remove the min weight vertex as well as its linked edges
# in the process, the most value is just the results we need
###

import heapq

N, M = input().split()
N, M = int(N), int(M)

arr = input().split()
arr = [int(i) for i in arr]

edges = [[] for _ in range(N)]
sums = [0 for _ in range(N)]

for i in range(M):
    ui, vi = input().split()
    ui, vi = int(ui), int(vi)
    ui -= 1
    vi -= 1
    edges[ui].append(vi)
    edges[vi].append(ui)
    sums[ui] += arr[vi]
    sums[vi] += arr[ui]

used = [False for _ in range(N)]
shq = [[sum, i] for i, sum in enumerate(sums)]
heapq.heapify(shq)
maxv = 0

for i in range(N):
    while True:
        sum, idx = heapq.heappop(shq)
        if not used[idx] and sums[idx] == sum:
            break
    maxv = max(maxv, sum)
    for vi in edges[idx]:
        if not used[vi]:
            sums[vi] -= arr[idx]
            heapq.heappush(shq, [sums[vi], vi])
    used[idx] = True

print(maxv)

