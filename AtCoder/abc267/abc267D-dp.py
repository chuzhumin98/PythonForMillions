###
# Solution: dp
# a simple dp, let f(n, k) be the max value with k value selected from a[:n], then
# f(n, k) = max( f(n-1, k), f(n-1, k-1) + k * a[n])
###
N, M = input().split()
N, M = int(N), int(M)
arr = input().split()
arr = [int(i) for i in arr]
MINF = -(1<<40)
fs = [MINF for _ in range(M+1)]
fs[0] = 0
for num in arr:
    for i in range(M-1, -1, -1):
        if fs[i] != MINF:
            fs[i+1] = max(fs[i+1], fs[i] + (i+1) * num)
print(fs[M])

