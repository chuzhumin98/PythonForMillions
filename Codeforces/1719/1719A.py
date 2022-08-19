###
# simple problem, no need to say
###
t = int(input())
for _ in range(t):
    x, y = input().split()
    x, y = int(x), int(y)

    if (x + y) % 2 == 0:
        print('Tonya')
    else:
        print('Burenka')
