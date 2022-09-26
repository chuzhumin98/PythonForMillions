t = int(input())
for _ in range(t):
    arr = input().split()
    arr = [int(i) for i in arr]

    res1, res2 = arr[0] * arr[3], arr[1] * arr[2]
    if res1 == res2:
        print(0)
    elif res1 == 0 or res2 == 0:
        print(1)
    elif res1 % res2 == 0 or res2 % res1 == 0:
        print(1)
    else:
        print(2)