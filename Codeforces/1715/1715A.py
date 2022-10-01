

t = int(input())
for _ in range(t):
    n, m = input().split()
    n, m = int(n), int(m)
    min_v = min(m, n) - 1
    if max(m, n) - 1 > 1:
        min_v += 1
    else:
        min_v = m + n - 2
    print(n + m - 2 + min_v)