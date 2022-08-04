###
# Solution:
# we can find that when the last digit number is 1, 2, 3, 4, 6, 7, 8, 9, when it goes after several turns, it will enter
# it 2, 4, 8, 6, 2, 4, 6, 8, .... last digit cycled.
# at the same time, we find that 2, 4, 8, 16 will go into 22, 42, 62, 82, ...
# 12, 14, 18, 26 will go into 32, 52, 72, 92, ...
# so that we can split them into (odd)2 and (even)2 groups.
# as for xxxx5 and xxxx0 number, we can find that when the last digit goes into 0, the number would be constant
# In a nutshell, the number could be group into (odd)2, (even)2, 0, 10, 20, 30, 40, ...
###

def get_type(num):
    if num % 10 not in [5, 0]:
        while True:
            if num % 10 == 2:
                break
            num += num % 10
        if (num // 10) % 2 == 0:
            return 2 # (even)2 group
        else:
            return 1 # (odd)2 group
    else:
        num += num % 10 # xxx0 group
        return num

t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().strip().split()
    arr = [int(_) for _ in arr]

    if n == 1:
        print("YES")
    else:
        current_type = get_type(arr[0])
        is_same_type = True
        for num in arr[1:]:
            if get_type(num) != current_type:
                is_same_type = False
                break
        if is_same_type:
            print("YES")
        else:
            print("NO")