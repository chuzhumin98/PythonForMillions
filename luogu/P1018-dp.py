###
# Solution: dp
# let f(n, k) be the max value for s[:n+1] with k divide
# we can get the recursive formula to be: f(n, k) = max_i(f(i, k-1) * s[i+1:n+1]),
# where i \in [k-1, n-1] is the last divide for s[:n+1]
# edge condition: f(n, 0) = int(s[:n+1]), f(n, k) = 0 if n < k
# complexity: O(K*N^2)
###

N, K = input().split()
N, K = int(N), int(K)

s = input().strip()

# f(n, k) = max_i(f(n-i, k-1) * s[n-i+1:n+1])
max_values = [[0 for _ in range(K+1)] for __ in range(N)]
for i in range(N):
    max_values[i][0] = int(s[:i+1])

for k in range(1, K+1):
    for n in range(k, N):
        for i in range(k-1, n):
            max_values[n][k] = max(max_values[n][k], max_values[i][k-1] * int(s[i+1:n+1]))

print(max_values[N-1][K])