###
# Solution: math + construction
# we find that 4k, 4k + 1, 4k + 3, 4k + 2 is a four ele tuples to support odd xor equals to even xor,
# as (4k) ^ (4k+3) = (4k+1) ^ (4k+2) = 3
# thus for n = 4k or 4k+1, we can use different k = 1, 2, ... ,k/4 to construct the array (append 0 if n = 4k+1);
# for n = 4k+2 or 4k+3, we need to supplement a six ele tuples [4+S, 1+S, 2+S, 12+S, 3+S, 8+S], where S is big enough to
# make them different to the simple 4k+p nums
###
t = int(input())
S = 1 << 20
res = [4+S, 1+S, 2+S, 12+S, 3+S, 8+S]
for _ in range(t):
    n = int(input())
    if n == 3:
        print('2 1 3')
    elif n % 4 <= 1:
        arr = []
        for i in range(n // 4):
            arr.append(4*i + 4)
            arr.append(4 * i + 5)
            arr.append(4 * i + 7)
            arr.append(4 * i + 6)
        if n % 4 == 1:
            arr.append(0)
        print(' '.join([str(i) for i in arr]))
    else:
        arr = []
        for i in range((n-6) // 4):
            arr.append(4*i+4)
            arr.append(4 * i + 5)
            arr.append(4 * i + 7)
            arr.append(4 * i + 6)
        arr += res
        if n % 2 == 1:
            arr.append(0)
        print(' '.join([str(i) for i in arr]))
