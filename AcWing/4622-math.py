###
# Solution: math
# Goldbach's conjecture: each no less than 6 even number can be splitted into two primes (f(n) is no more than 2);
# each no less than 7 can be divided into three primes (f(n) is no more than 3),
# then we just need to confirm if odd n can be divided into 1 (n is prime) or 2 (n-2 is prime), to obtain the result
###
def is_prime(n):
    for m in range(2, n):
        if m * m > n:
            break
        if n % m == 0:
            return False
    return True

n = int(input())
ans = {2: 1, 3: 1, 4: 2, 5: 1, 6: 2, 7: 1}

if n in ans:
    print(ans[n])
elif n % 2 == 0:
    print(2)
else:
    if is_prime(n):
        print(1)
    elif is_prime(n-2):
        print(2)
    else:
        print(3)