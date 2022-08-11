###
# Solution:
# we can regard two soldier continue to move in original direction (see it as soul exchange)
# then the min time and max time is clear to see!
###

L = int(input())
N  = int(input())
if N == 0:
    print("0 0")
else:
    arr = input().split()
    arr = [int(_) for _ in arr]
    arr.sort()

    time_max = max(arr[-1], L+1-arr[0])
    time_min = 0
    for num in arr:
        time_min = max(time_min, min(num, L+1-num))

    print(f'{time_min} {time_max}')