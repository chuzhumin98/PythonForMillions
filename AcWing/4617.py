T = int(input())
for _ in range(T):
    a = int(input())
    _sum = 1
    while a > 0:
        if a % 2 == 1:
            _sum *= 2
        a //= 2
    print(_sum)