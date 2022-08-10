###
# simple problem, no need to say
###

t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().split()
    arr = [int(i) for i in arr]

    increaseMode = True
    isMin = True
    for i in range(len(arr) - 1):
        if increaseMode and arr[i+1] < arr[i]:
            increaseMode = False
        if not increaseMode and arr[i+1] > arr[i]:
            isMin = False
            break
    print("YES" if isMin else "NO")
