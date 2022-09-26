t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().split()
    arr = [int(i) for i in arr]

    arr.sort()
    print(arr[-1] + arr[-2] - arr[0] - arr[1])