###
# simple problem, no need to say
###

t = int(input())
square_nums = [a * a for a in range(1000)]
noless_squares_nums_dict = {0: 0, 1: 1}
idx = 2
for i in range(2, 100000+5):
    if i > square_nums[idx]:
        idx += 1
    noless_squares_nums_dict[i] = square_nums[idx]


for _ in range(t):
    n = int(input())
    permuatation = [-1] * n

    concerned_num = n - 1
    while True:
        if concerned_num <= 0:
            for i in range(concerned_num + 1):
                permuatation[i] = i
            break

        pair_num = noless_squares_nums_dict[concerned_num] - concerned_num

        for i in range(concerned_num - pair_num + 1):
            permuatation[pair_num + i] = concerned_num - i

        concerned_num = pair_num - 1

    print(' '.join([str(i) for i in permuatation]))

