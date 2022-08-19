###
# simple problem, no need to say
###
t = int(input())

for _ in range(t):
    n, k = input().split()
    n, k = int(n), int(k)

    if k % 2 == 1:
        print("YES")
        for i in range(n // 2):
            print(f'{i * 2 + 1} {i * 2 + 2}')
    elif k % 4 == 0:
        print("NO")
    else:
        print("YES")
        for i in range(n // 2):
            if i % 2 == 0:
                print(f'{i * 2 + 2} {i * 2 + 1}')
            else:
                print(f'{i * 2 + 1} {i * 2 + 2}')