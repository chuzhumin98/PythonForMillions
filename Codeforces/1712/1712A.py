###
# simple problem, no need to say
###
t = int(input())
for _ in range(t):
    n, k = input().split()
    n, k = int(n), int(k)

    ps = input().split()
    ps = [int(i) for i in ps]

    _sum = 0
    for num in ps[:k]:
        if num > k:
            _sum += 1
    print(_sum)