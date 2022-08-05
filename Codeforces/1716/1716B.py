###
# simple problem, no need to say
###

t = int(input())
for _ in range(t):
    n = int(input())
    print(n)

    array = list(range(1,n+1))
    print(' '.join([str(i) for i in array]))
    for i in range(n - 1):
        array[i + 1], array[0] = array[0], array[i + 1]
        print(' '.join([str(i) for i in array]))