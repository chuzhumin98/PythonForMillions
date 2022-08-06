###
# Solution:
# if the total edge (friend relation) number is even, then we no need to delete point (uninvite people)
# if the total edge number is odd, we have two ways to delete point to make it become even:
# 1. delete one odd degree point;
# 2. delete two even degree points, and there exists one edge to link them
# our task is to find the min value of the above two ways
###

t = int(input())
for _ in range(t):
    n, m = input().split()
    n, m = int(n), int(m)

    As = input().split()
    As = [int(i) for i in As]

    edges = [[] for _ in range(n)]
    for __ in range(m):
        a, b = input().split()
        a, b = int(a), int(b)
        edges[a-1].append(b-1)
        edges[b-1].append(a-1)


    if m % 2 == 0:
        print(0)
    else:
        As_with_idx = [[a, i] for i, a in enumerate(As)]
        As_with_idx.sort(key=lambda x:x[0])

        min_cost = 1000000

        selected_set = set()
        for a, idx in As_with_idx:
            if a > min_cost:
                break
            if len(edges[idx]) % 2 == 1:
                min_cost = min(min_cost, a)
                break
            else:
                for e in edges[idx]:
                    if e in selected_set:
                        min_cost = min(min_cost, As[e] + a)

            selected_set.add(idx)

        print(min_cost)