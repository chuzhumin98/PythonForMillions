###
# Solution:
# if we leave m ( and n ), then place them as ( ( ( ( ) ) ) is certainly one valid way (as the problem exist at least one way).
# then for other condition, the easiest satisfied way is ( ( ( ) ( ) ), as the prefix number of ( minus the prefix number of ) is second-larger with this way.
# so we just need to check if this way can be satisfied, to get the uniqueness
###

t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)

    left_bracket_num = n // 2
    right_bracket_num = n // 2
    for char in s:
        if char == '(':
            left_bracket_num -= 1
        elif char == ')':
            right_bracket_num -= 1

    if left_bracket_num == 0 or right_bracket_num == 0:
        print("YES")
    else:
        sum_before_qs = []
        _sum = 0
        idx = -1
        for idx, char in enumerate(s):
            if char == '(':
                _sum += 1
            elif char == ')':
                _sum -= 1
            else:
                sum_before_qs.append(_sum + len(sum_before_qs))
                if len(sum_before_qs) == left_bracket_num:
                    break

        if sum_before_qs[-1] < 1:
            print("YES")
        else:
            current_value = sum_before_qs[-1] - 1
            while True:
                idx += 1
                if s[idx] == '?':
                    print("NO")
                    break
                elif s[idx] == '(':
                    current_value += 1
                else:
                    current_value -= 1
                    if current_value < 0:
                        print("YES")
                        break
