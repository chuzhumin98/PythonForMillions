###
# simple problem, no need to say
###

t = int(input())
for _ in range(t):
    x = int(input())
    arr = input().split()
    arr = [int(_) for _ in arr]

    opened = [0, 0, 0]
    while True:
        if x == 0:
            break
        opened[x-1] = 1
        x = arr[x-1]

    if sum(opened) == 3:
        print("YES")
    else:
        print("NO")