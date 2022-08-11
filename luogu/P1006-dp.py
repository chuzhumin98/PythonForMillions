###
# Solution: dp
# as the two paths could not have same point, we can just ensure for any _sum \in [1, m+n-3], the point file {(x, y) | x + y = _sum}
# has two different point, then do DP just satisfy the requirments.
# let f(sum, x1, x2) be the max value when two paths both from (0, 0), then come to (x1, sum-x1) and (x2, sum-x2) respectively, where x1 < x2
# the recursive formula is: f(sum, x1, x2) = max(f(sum, x1-1, x2-1), f(sum, x1-1, x2), f(sum, x1, x2-1), f(sum, x1, x2)) + A(x1, sum-x1) + A(x2, sum-x2)
# the max set just take the valid parts.
# then the value f(m+n-3, m-2, m-1) is the right answer!
###

m, n = input().split()
m, n = int(m), int(n)

matrix = []
for _ in range(m):
    arr = input().split()
    arr = [int(__) for __ in arr]
    matrix.append(arr)

if min(m, n) == 1:
    print(0)
else:
    pred_arr = {0: {1: matrix[0][1] + matrix[1][0]}}
    current_arr = {0: {1: matrix[0][1] + matrix[1][0]}}
    _sum = 1
    rightbottom_num = m + n - 2
    while True:
        if _sum >= rightbottom_num:
            break
        new_arr = {}
        for row_1 in range(max(0, _sum - n + 1), min(m-1, _sum) + 1):
            for row_2 in range(row_1+1, min(m-1, _sum) + 1):
                if row_1 not in new_arr:
                    new_arr[row_1] = dict()
                col_1 = _sum - row_1
                col_2 = _sum - row_2
                max_value = 0
                if row_1 > 0:
                    if row_2 > 0:
                        max_value = max(current_arr[row_1-1][row_2-1], max_value)
                    if col_2 > 0:
                        max_value = max(current_arr[row_1 - 1][row_2], max_value)
                if col_1 > 0:
                    if col_2 > 0:
                        max_value = max(current_arr[row_1][row_2], max_value)
                    if row_2 > 0 and row_2 - 1 != row_1:
                        max_value = max(current_arr[row_1][row_2-1], max_value)
                new_arr[row_1][row_2] = max_value + matrix[row_1][col_1] + matrix[row_2][col_2]

        pred_arr = current_arr
        current_arr = new_arr

        _sum += 1

    print(current_arr[m-2][m-1])


