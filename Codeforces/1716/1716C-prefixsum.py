###
# Solution: prefixsum
# no that for the matrix 2*m, the valid path number is only m! That is:
#  .    . -> .    . <- . <- .
#  |    ^    |              ^
#  v    |    v              |
#  . -> .    . -> . -> . -> .
# The left i-th column is the zig-zag path, and the remained m - i column is one cycle
# To use O(1) time to get the min time of each path, we need to calculate the postfix min time
# to move from (k, m) -> (k, i) and (k, i) -> (k, m), denote them as f1(k, i) and f2(k, i) respectively,
# the recursive formula for them is: f1(k, i) = max(f1(k, i+1) + 1, arr(k, i)),
# f2(k, i) = max(f2(k, i+1), arr(k, i) + m - i)
# then if we zig-zag-ly reached (k, i) in time t to consider for a cycle, to reach (k, m) the min-time is A = max(f2(k, i), t + m - i)
# then to complete the visit action, the min-time is B = max(f1(1-k, i), A + 1 + m - i)
# finally, we only need to take the min B for each i, that is the returned min value
###

t = int(input())
for _ in range(t):
    m = int(input())
    arr = [0, 0]
    arr[0] = input().strip().split()
    arr[1] = input().strip().split()
    arr[0] = [int(_) for _ in arr[0]]
    arr[1] = [int(_) for _ in arr[1]]

    row_left_time = [[0 for ___ in range(m)] for __ in range(2)] # m-1 -> i
    row_right_time = [[0 for ___ in range(m)] for __ in range(2)] # i -> m - 1

    for i in range(2):
        row_right_time[i][-1] = arr[i][-1] + 1
        for j in range(1, m):
            if j == m - 1 and i == 0:
                row_right_time[i][m - 1 - j] = max(row_right_time[i][m - j], arr[i][m - 1 - j] + j)
            else:
                row_right_time[i][m - 1 - j] = max(row_right_time[i][m - j], arr[i][m - 1 - j] + 1 + j)

    for i in range(2):
        row_left_time[i][-1] = arr[i][-1] + 1
        for j in range(1, m):
            row_left_time[i][m-1-j] = max(row_left_time[i][m-j]+1, arr[i][m-1-j] + 1)
    # print(row_left_time, row_right_time)
    _min_time = 1 << 30 + 1000000
    current_time = 0
    for i in range(m-1):
        if i % 2 == 0:
            rightbelow_time = max(row_right_time[0][i], m-1-i+current_time) + 1
            finished_time = max(row_left_time[1][i], rightbelow_time+m-1-i)
            # print(i, ':', finished_time, current_time)
            _min_time = min(_min_time, finished_time)

            current_time = max(current_time + 2, arr[1][i] + 2, arr[1][i+1] + 1)
        else:
            rightup_time = max(row_right_time[1][i], m-1-i+current_time) + 1
            finished_time = max(row_left_time[0][i], rightup_time + m - 1 - i)
            _min_time = min(_min_time, finished_time)
            # print(i, ':', finished_time, current_time)

            current_time = max(current_time + 2, arr[0][i] + 2, arr[0][i + 1] + 1)

    if m % 2 == 0:
        current_time = max(current_time+1, arr[0][-1]+1)
    else:
        current_time = max(current_time + 1, arr[1][-1]+1)
    # print('current:', current_time)
    _min_time = min(_min_time, current_time)

    print(_min_time)






