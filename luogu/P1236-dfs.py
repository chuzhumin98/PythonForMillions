###
# Solution: bruteforce + DFS
# You just need to try all the digit permutation and operation
# note that for the permutation a, b, c, d; first you can calculate a ~ b -> e, then e ~ c and c ~ d are two
# types you need to consider; you can use DFS to search for all operation paths
###

def get_next_permutation(arr):
    arr_right = [arr[-1]]
    idx = len(arr) - 2
    while True:
        if idx < 0:
            return None
        if arr[idx] < arr_right[-1]:
            break
        arr_right.append(arr[idx])
        idx -= 1
    concerned_value = arr[idx]
    idx_swap = 0
    while True:
        if arr_right[idx_swap] > concerned_value:
            break
        idx_swap += 1
    arr_right[idx_swap], concerned_value = concerned_value, arr_right[idx_swap]
    arr_new = [num for num in arr[:idx]]
    arr_new.append(concerned_value)
    arr_new += arr_right
    return arr_new

def try_24_point(arr, current_cals, valid_cals_list):
    if len(arr) == 1:
        if arr[0] == 24:
            valid_cals_list.append([expr1 for expr1 in current_cals])
        return
    a, b = arr.pop(), arr.pop()

    arr.append(a + b)
    current_cals.append('+')
    try_24_point(arr, current_cals, valid_cals_list)

    if a >= b:
        arr[-1] = a - b
        current_cals[-1] = '-'
        try_24_point(arr, current_cals, valid_cals_list)

    if a <= b:
        arr[-1] = b - a
        current_cals[-1] = '|-'
        try_24_point(arr, current_cals, valid_cals_list)

    arr[-1] = a * b
    current_cals[-1] = '*'
    try_24_point(arr, current_cals, valid_cals_list)

    if b != 0 and a % b == 0:
        arr[-1] = a // b
        current_cals[-1] = '/'
        try_24_point(arr, current_cals, valid_cals_list)

    if a != 0 and b % a == 0:
        arr[-1] = b // a
        current_cals[-1] = '|/'
        try_24_point(arr, current_cals, valid_cals_list)

    current_cals.pop()
    arr[-1] = b
    arr.append(a)

    if len(arr) == 3:
        a, b = arr.pop(0), arr.pop(0)
        arr.append(a + b)
        current_cals.append('>+')
        try_24_point(arr, current_cals, valid_cals_list)

        if a >= b:
            arr[-1] = a - b
            current_cals[-1] = '>-'
            try_24_point(arr, current_cals, valid_cals_list)

        if a <= b:
            arr[-1] = b - a
            current_cals[-1] = '>|-'
            try_24_point(arr, current_cals, valid_cals_list)

        arr[-1] = a * b
        current_cals[-1] = '>*'
        try_24_point(arr, current_cals, valid_cals_list)

        if b != 0 and a % b == 0:
            arr[-1] = a // b
            current_cals[-1] = '>/'
            try_24_point(arr, current_cals, valid_cals_list)

        if a != 0 and b % a == 0:
            arr[-1] = b // a
            current_cals[-1] = '>|/'
            try_24_point(arr, current_cals, valid_cals_list)

        current_cals.pop()
        arr.pop()
        arr.insert(0, b)
        arr.insert(0, a)

def expr(a, b, cal):
    if cal == '+':
        return a + b
    elif cal == '-':
        return a - b
    elif cal == '|-':
        return b - a
    elif cal == '*':
        return a * b
    elif cal == '/':
        return a // b
    else:
        return b // a



arr = input().split()
arr = [int(_) for _ in arr]

solved = False
permutation = [0, 1, 2, 3]
while True:
    arr_P = [arr[idx] for idx in permutation]
    arrP_copy = [num for num in arr_P]
    # TODO: try all computation
    valid_cals_list = []
    try_24_point(arrP_copy, [], valid_cals_list)
    if len(valid_cals_list) > 0:
        one_cals = valid_cals_list[0]
        for i in range(3):
            cal_this = one_cals[i]
            if cal_this[0] == '>':
                a, b = arr_P.pop(0), arr_P.pop(0)
                cal_this = cal_this[1:]
            else:
                a, b = arr_P.pop(), arr_P.pop()

            result = expr(a, b, cal_this)
            if cal_this[0] == '|':
                print(f'{max(a, b)}{cal_this[1]}{min(a, b)}={result}')
            else:
                print(f'{max(a, b)}{cal_this}{min(a, b)}={result}')

            arr_P.append(result)
        solved = True
        break



    if solved:
        break

    permutation = get_next_permutation(permutation)
    if not permutation:
        break

if not solved:
    print("No answer!")