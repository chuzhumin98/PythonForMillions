###
# Solution: Tree-like Array
# first we sort all rectangle (constraints low and high bounds) width in increasing order: using backet sort,
# then in the width increasing order, we need to satisfy two operations:
# (1) insert a rectangle (height: h, area: w * h
# (2) calculate the prefix sum: sum_Area(h <= H), as the width handles with increasing order, then
# sum_Area(h <= H_b-1) [current with = W_b and hasnot insert W_b width recs] - sum_Area(h <= H_s) [current with = W_s and has insert
# W_s width recs] is just the result we need.
# To support the above two types of operations in O(log n) complexity, we use tree-like array data structure
###
def lowbit(n):
    return n & (-n)

def prefix_sum(tree_list, n): # sum(a[:n+1]
    _sum = 0
    while n > 0:
        _sum += tree_list[n]
        n -= lowbit(n)
    return _sum

def addwith(tree_list, n, num): # a[n] += num
    while n < len(tree_list):
        tree_list[n] += num
        n += lowbit(n)

NMAX = 1001
t = int(input())
for _ in range(t):
    n, q = input().split()
    n, q = int(n), int(q)
    recs = [[] for i in range(NMAX)]
    qs_in = [[] for i in range(NMAX)]
    qs_out = [[] for i in range(NMAX)]
    for i in range(n):
        hi, wi = input().split()
        hi, wi = int(hi), int(wi)
        recs[hi].append(wi)
    for i in range(q):
        hs, ws, hb, wb = input().split()
        hs, ws, hb, wb = int(hs), int(ws), int(hb), int(wb)-1
        qs_in[hs].append([ws, wb, i])
        qs_out[hb-1].append([ws, wb, i])
    _ans = [0 for i in range(q)]

    tree_list = [0 for _ in range(NMAX)]
    for h in range(1, NMAX):
        for wi in recs[h]:
            addwith(tree_list, wi, wi * h)
        for ws, wb, idx in qs_in[h]:
            val = prefix_sum(tree_list, wb) - prefix_sum(tree_list, ws)
            _ans[idx] -= val
        for ws, wb, idx in qs_out[h]:
            val = prefix_sum(tree_list, wb) - prefix_sum(tree_list, ws)
            _ans[idx] += val
    for ans in _ans:
        print(ans)


