###
# Solution:
# note that if we have two "0" in a 2*2 square, then we can erase only one "1" in a step, the max total step num is the
# number of "1" (denote k);
# if only one "0" in a 2*2 square, in the first time we need to erase two "1"'s and then only one in each step,
# that is k - 1 steps;
# if none of "0" in the grids, then in the first time we need to erase three "1"'s and then only one in each step,
# that is k - 2 steps;
###
t = int(input())
for _ in range(t):
    n, m = input().split()
    n, m = int(n), int(m)

    s = []
    for i in range(n):
        ss = input().strip()
        ss = [int(char) for char in ss]
        s.append(ss)

    one_num = sum([sum(row) for row in s])
    hasZero = False if one_num == m * n else True
    has_row2zero = True if min([min([row[i] + row[i+1] for i in range(m-1)]) for row in s]) == 0 else False
    has_col2zero = True if min([min([s[i][j] + s[i+1][j] for i in range(n-1)]) for j in range(m)]) == 0 else False
    has_xie2zero = False
    for i in range(n-1):
        for j in range(m-1):
            if s[i][j] == 0 and s[i+1][j+1] == 0:
                has_xie2zero = True
                break
            if s[i+1][j] == 0 and s[i][j+1] == 0:
                has_xie2zero = True
                break
    if has_row2zero or has_col2zero or has_xie2zero:
        print(one_num)
    elif hasZero:
        print(one_num - 1)
    else:
        print(one_num - 2)
