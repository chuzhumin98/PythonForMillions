t = int(input())
for _ in range(t):
    n, k, r, c = input().split()
    n, k, r, c = int(n), int(k), int(r), int(c)
    r -= 1
    c -= 1
    r %= k
    c %= k
    matrix = [['.' for _ in range(n)] for __ in range(n)]
    for rid in range(n // k):
        radd = rid * k
        for cid in range(n // k):
            cadd = cid * k
            for i in range(k):
                matrix[radd + i][cadd + i] = 'X'
            matrix[radd+r][cadd+r] = '.'
            matrix[radd+c][cadd+c] = '.'
            matrix[radd+r][cadd+c] = 'X'
            matrix[radd+c][cadd+r] = 'X'
    for i in range(n):
        print(''.join(matrix[i]))