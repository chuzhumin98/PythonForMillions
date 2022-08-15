###
# Solution: dp (0-1 bag problem), TLE with python code
# f(i, j, k) store whether or not we can select from j items from As[:i] to obtain the sum k, then
# f(i, j, k) = f(i, j, k) or f(i-1, j-1, k-As[i))
# note that i-dim is unnecessary when we iter j and k from large to small, that is f(j, k) = f(j, k) or f(j-1, k-As[j])
# the result of sum k can be obtained is f(n, n/2, k), then we only need to choose the best k;
# Complexity: O(n * n/2 * sum(As)), the worst case is O(20*n^3)
###

n = int(input())
As = []
for _ in range(n):
    As.append(int(input()))

if n == 1:
    print(0, As[0])
else:
    As.sort()
    if len(As) % 2 == 0:
        delta = As[0]
        sidx = 0
        for i in range(sidx, n):
            As[i] -= delta
    else:
        delta = 0
        sidx = 0

    select_num = n // 2
    total_sum = sum(As)

    fs = [[False for __ in range(total_sum + 1)] for _ in range(select_num + 1)]
    fs[0][0] = True
    for ai in As:
        for k in range(select_num, 0, -1):
            for _sum in range(total_sum, ai-1, -1):
                fs[k][_sum] = fs[k-1][_sum-ai] or fs[k][_sum]
        # print([_sum for _sum in range(total_sum + 1) if fs[select_num][_sum]])



    delta_bloods = [[abs(2 * _sum - total_sum), _sum] for _sum in range(total_sum+1) if fs[select_num][_sum]]
    delta_this, _sum = min(delta_bloods, key=lambda x:x[0])
    print(_sum + delta * (n // 2), total_sum - _sum + delta * (n // 2))

