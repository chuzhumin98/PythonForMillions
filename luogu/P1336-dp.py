###
# Solution: DP
# a simple dp, let f(m, n) be the min time to complete n paper with first-m project, then we consider all
# different possibilities of paper number for the last project.
# The recursive formula could be: f(m, n) = min_k ( f(m-1, k) + A[m] * (n-k)^B[m] )
###

INF = 1e13
n, m = input().split()
n, m = int(n), int(m)

A, B = [], []
for i in range(m):
    a, b = input().split()
    a, b = int(a), int(b)
    A.append(a)
    B.append(b)

fs = [[INF for __ in range(n+1)] for _ in range(m)] # fs[i][j], i: project, j: paper, fs: min time
for j in range(n+1):
    fs[0][j] = A[0] * (j ** B[0])
for i in range(1, m):
    for j in range(n+1):
        for k in range(j+1):
            fs[i][j] = min(fs[i][j], fs[i-1][k] + A[i] * ((j-k) ** B[i]))

print(fs[m-1][n])

