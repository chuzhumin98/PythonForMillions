###
# Solution: dp
# simple dp thinking: let f(n) be the min rock use when finally the frog locates at position n
# so that f(n) = min_{S <= k <= T}f(n-k) + I(n has rock), where I(n has rock) = 1 when n has rock, else is 0
# we can find the complexity is O((T-S)*10^9), TLE!!!
# to reduce complexity, we find that when the distance of neighbor two rocks is far enough,
# we can just split them, then first compute the min value of left, then move towards a near eough position to consider the right one
# a simple threshold is 9 * 10 + 10 = 100, we can narrow every neighbor distance more than 100 to 100,
# then we only need to consider the total distance is 100 * M = 10^4, the complexity is no more than 10^5, AC!
###

L = int(input())
S, T, M = input().split()
S, T, M = int(S), int(T), int(M)
rocks = input().split()
rocks = [int(_) for _ in rocks]



if S == T: # certain
    cnt = 0
    for num in rocks:
        if num % S == 0 and num <= L:
            cnt += 1
    print(cnt)
else:
    delta = 100  # if d > delta, then we can start from any position

    rocks.sort()
    rocks_dict = {}
    for rock in rocks:
        rocks_dict[rock] = 0
    current_position = max(0, rocks[0] - delta)
    current_min_rocks = 0
    current_rock_id = 1


    while True:
        if current_rock_id >= len(rocks) or rocks[current_rock_id] - rocks[current_rock_id-1] >= delta:
            # handle this rock list
            N_this = rocks[current_rock_id - 1] - current_position + 10
            min_rocks_list = [1000 for _ in range(N_this)]
            min_rocks_list[0] = current_min_rocks
            for idx in range(S, N_this):
                min_rocks_list[idx] = min(min_rocks_list[max(idx-T, 0):idx-S+1])
                if (idx + current_position) in rocks_dict:
                    min_rocks_list[idx] += 1

            current_min_rocks = min(min_rocks_list[N_this-11:])
            current_rock_id += 1
            if current_rock_id >= len(rocks):
                break
            current_position = rocks[current_rock_id-1] - delta
        else:
            current_rock_id += 1

    print(current_min_rocks)



