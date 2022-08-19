###
# Solution: dp, TLE with python
# a similar problem with https://leetcode.cn/problems/edit-distance/
# let f(m, n) be the min distance of sA[:m] and sB[:n], then
# f(m, n) = min(f(m-1, n) + K, f(m, n-1) + K, f(m-1, n-1) + abs(sA[m] - sB[n]))
# complexity: O(K*N^2)
###

sA = input().strip()
sB = input().strip()
K = int(input())

M, N = len(sA), len(sB)

distances = [[0 for _ in range(N+1)] for __ in range(M+1)]
for i in range(N+1):
    distances[0][i] = i * K
for i in range(M+1):
    distances[i][0] = i * K

for i in range(1, M+1):
    for j in range(1, N+1):
        distances[i][j] = min(distances[i-1][j] + K, distances[i][j-1] + K, distances[i-1][j-1] + abs(ord(sA[i-1]) - ord(sB[j-1])))

print(distances[M][N])
