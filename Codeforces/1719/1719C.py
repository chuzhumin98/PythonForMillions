###
# Solution:
# we need to only consider the front n - 1 rounds completes, as after this only the largest one can win all the game.
# we first visit all the competitor, to record their win times in front n-1 rounds.
# note that one competitor k can only stand for fights once (some continued rounds), his first fight is at max(k, 1) round.
# so for each query, we can just find the intersection time between [1, t] and [k, win[k]+k-1]
# if t > n - 1, we need to add the win number for the largest person with t - n + 1
###
t = int(input())
for _ in range(t):
    n, q = input().split()
    n, q = int(n), int(q)
    arr = input().split()
    arr = [int(i) for i in arr]
    wins_times = [0 for _ in range(n)]
    if arr[0] < arr[1]:
        wins_times[1] += 1
        win_now = 1
    else:
        wins_times[0] += 1
        win_now = 0

    for i in range(2, n):
        if arr[i] > arr[win_now]:
            wins_times[i] += 1
            win_now = i
        else:
            wins_times[win_now] += 1

    # print(wins_times)
    # wins_times[win_now] += 1

    for __ in range(q):
        i, k = input().split()
        i, k = int(i)-1, int(k)
        k_first = min(k, n-1)
        k_last = k - k_first
        win_time = 0
        if i == 0:
            ii = i + 1
        else:
            ii = i
        if ii <= k_first:
            win_time = min(k_first - ii + 1, wins_times[i])

        if win_now == i:
            win_time += k_last

        print(win_time)

