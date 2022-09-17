T = int(input())
for _ in range(T):
    x, y, a, b = input().split()
    x, y, a, b = int(x), int(y), int(a), int(b)
    if (y - x) % (a + b) != 0:
        print(-1)
    else:
        print((y-x)//(a +b))