###
# simple problem, no need to say
###
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(range(1, n+1))
    delta = n % 2
    for i in range(n // 2):
        low = delta + i * 2
        high = low + 1
        arr[low], arr[high] = arr[high], arr[low]
    print(' '.join([str(i) for i in arr]))