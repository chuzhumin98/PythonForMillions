###
# simple problem, no need to say
###

t = int(input())
for _ in range(t):
    n = int(input())
    max_distance = [0] * 4 # x, -x, y, -y
    for __ in range(n):
        xi, yi = input().split()
        xi, yi = int(xi), int(yi)

        if xi == 0:
            if yi >= 0:
                idx = 2
            else:
                idx = 3
        else:
            if xi >= 0:
                idx = 0
            else:
                idx = 1

        max_distance[idx] = max(max_distance[idx], abs(xi) + abs(yi))

    print(2 * sum(max_distance))