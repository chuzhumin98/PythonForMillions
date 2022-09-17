t = int(input())
for _ in range(t):
    arr = input().split()
    n, m, sx, sy, d = [int(o) for o in arr]
    if sx - d <= 1 and sx + d >= n:
        print(-1)
    elif sy - d <= 1 and sy + d >= m:
        print(-1)
    elif sx - d <= 1 and sy - d <= 1:
        print(-1)
    elif sx + d >= n and sy + d >= m:
        print(-1)
    else:
        print(n + m - 2)