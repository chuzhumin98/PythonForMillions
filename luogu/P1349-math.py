###
# Solution: math + quick power
# let A(n) = [a_{n}, a_{n-1}], M = [[p, q], [1, 0]]
# we can find that A(n+1) = M * A(n), so A(n+1) = M^n * A(1)
# thus, we can use quick power to calculate a_n in O(log n) time
###

def multi_matrix(arr1, arr2, m):
    arr = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            arr[i][j] = (arr1[i][0] * arr2[0][j] + arr1[i][1] * arr2[1][j]) % m
    return arr

arr = input().split()
p, q, a1, a2, n, m = [int(i) for i in arr]

if n <= 2:
    value = a1 if n == 1 else a2
    print(value % m)
else:
    A = [a2, a1]
    M_final = [[1, 0], [0, 1]]
    M = [[p, q], [1, 0]]
    # a_n = M^(n-2) * A the first item
    mi = n - 2
    while mi > 0:
        if mi % 2 == 1:
            M_final = multi_matrix(M, M_final, m)
        M = multi_matrix(M, M, m)
        mi = mi // 2

    value = (M_final[0][0] * A[0] + M_final[0][1] * A[1]) % m
    print(value)

