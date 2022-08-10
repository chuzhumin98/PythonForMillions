###
# Solution: construction, but TLE with python, so we recode with C++ and AC
# consider two simple condition:
# (1) 2 people: a, b. we only need to compare ? a b, to find the winner, 1 query, one query to cancel one person
# (2) 4 people: a, b, c, d (where a compete b first, c compete d first, then the winner of a,b compete the winner of c,d. we only need to compare two turns
# 2-1. ? a c
# if win(a) > win(c), then ? a d, the more win one is the winner of four people;
# if win(a) = win(c), then ? b d, the more win one is the winner of four people;
# if win(a) < win(c), then ? b c, the more win one is the winner of four people;
# 2 queries, 2 queries to cancel 3 people.
# so, we can use (2) to reduce people from 2^n -> 2^(n-2) -> 2^(n-4) -> ... -> 1 or 2 (use (1) to reduce the remain 2)
# the queries ratio is just no more than ceil value of 2^n * 2/3
###

import sys

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [i for i in range(1, (1<<n)+1)]
    while True:
        if len(arr) == 1:
            print(f"! {arr[0]}")
            sys.stdout.flush()
            break
        elif len(arr) == 2:
            print(f"? {arr[0]} {arr[1]}")
            sys.stdout.flush()
            flag = int(input())
            if flag == 1:
                print(f"! {arr[0]}")
            else:
                print(f"! {arr[1]}")
            sys.stdout.flush()
            break
        else:
            arr_new = []
            for i in range(len(arr) // 4):
                arr_slice = arr[4*i:4*(i+1)]
                print(f"? {arr_slice[0]} {arr_slice[2]}")
                sys.stdout.flush()
                flag = int(input())
                if flag == 1:
                    print(f"? {arr_slice[0]} {arr_slice[3]}")
                    sys.stdout.flush()
                    flag_2 = int(input())
                    if flag_2 == 1:
                        arr_new.append(arr_slice[0])
                    else:
                        arr_new.append(arr_slice[3])
                elif flag == 2:
                    print(f"? {arr_slice[1]} {arr_slice[2]}")
                    sys.stdout.flush()
                    flag_2 = int(input())
                    if flag_2 == 1:
                        arr_new.append(arr_slice[1])
                    else:
                        arr_new.append(arr_slice[2])
                else:
                    print(f"? {arr_slice[1]} {arr_slice[3]}")
                    sys.stdout.flush()
                    flag_2 = int(input())
                    if flag_2 == 1:
                        arr_new.append(arr_slice[1])
                    else:
                        arr_new.append(arr_slice[3])
            arr = arr_new

