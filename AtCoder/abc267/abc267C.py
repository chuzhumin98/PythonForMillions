N, M = input().split()
N, M = int(N), int(M)
arr = input().split()
arr = [int(i) for i in arr]
maxV = 0
for i in range(M):
    maxV += (i + 1) * arr[i]
_sum_m = sum(arr[:M])
val = maxV

for i in range(M, N):
    val += M * arr[i] - _sum_m
    maxV = max(maxV, val)
    _sum_m += arr[i] - arr[i-M]
print(maxV)

