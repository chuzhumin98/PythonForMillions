###
# simple problem, no need to say
###

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 1:
        print("2")
    else:
        print((n+2) // 3)