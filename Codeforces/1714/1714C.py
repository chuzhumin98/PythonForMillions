###
# Solution:
# This problem can be solved used the greedy algorithm, as the digit of the number can not be repeated. To get the smallest number, we can use 9, 8, 7, ..., 2, 1 in order, the head position is just the remained value.
# For example, when s = 20, as 20 > 9, we first take 9 of it as the digits, s_remain = 20 - 9 = 11; as 11 > 8, we take 8 of it as the tens, s_remain = 11 - 8 = 3; as 3 <= 7, then all of the 3 can be taken as the hundreds,
# the final number is 389
###

t = int(input())
for _ in range(t):
    num = ''
    current_max = 9

    s = int(input())

    while True:
        if s <= current_max:
            num = str(s) + num
            current_max -= 1
            s = 0
        else:
            num = str(current_max) + num
            s -= current_max
            current_max -= 1

        if s == 0:
            break
    print(num)