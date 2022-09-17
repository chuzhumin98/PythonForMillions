###
# Solution: greedy
# min of d_i: to find the min value b_k >= a_i, then d_i = b_k - a_i, as k must <= i, that cannot be contradictory
# max of d_i: to better incorporate with max d_i, that is match a_i -> b_k where k >= i,
# the best incorporation approach is a_{i+1} -> b_i, a_{i+2} -> b_{i+1}, ..., a_{k} -> b_{k-1}
# then we just only need to find the first k >= i such that a_{k+1} > b_{k}, then this is the k we need,
# max of d_i = b_k - a_i
###

t = int(input())
for _ in range(t):
    n = int(input())
    As = input().split()
    As = [int(i) for i in As]
    Bs = input().split()
    Bs = [int(i) for i in Bs]
    min_ds = []
    idx = 0
    for i, a in enumerate(As):
        while Bs[idx] < a:
            idx += 1
        min_ds.append(Bs[idx] - a)

    max_ds = []
    non_xies = [-1]
    for i in range(n-1):
        if As[i+1] > Bs[i]:
            non_xies.append(i)
    non_xies.append(n-1)

    for i in range(1, len(non_xies)):
        for idx in range(non_xies[i-1]+1, non_xies[i]+1):
            max_ds.append(Bs[non_xies[i]] - As[idx])

    print(' '.join([str(i) for i in min_ds]))
    print(' '.join([str(i) for i in max_ds]))
