###
# Solution: Category Discussion
# for a k-digit number n = a1 a2 a3 ... ak
# 1. the j-digit number, j < k, the total sum is 9 (first digit can not be zero) * 9 * 8 * 7 * ... * (11 - j)
# 2. the number between a1 ... ap 0 0 ... 0 to a1 ... ap ap+1 ... ak
# if a1 ... ap has repetitive digit, then total sum is zero; if not then
#   2.1 p+1-th digit is 0, 1, ..., ap+1 - 1, the p+2 to k digit can be any from 00..0 to  99..9;
#   2.2 p+1-th digit is ap+1, then goto 2.1 of next p <- p+1
###

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        digit_num = 1
        remain_num = n // 10
        digits_n = [n % 10]
        while True:
            if remain_num == 0:
                break
            digit_num += 1
            digits_n.append(remain_num % 10)
            remain_num //= 10

        _sum = 0
        total_digit_sum = 9
        for digit in range(1, digit_num):
            _sum += total_digit_sum
            total_digit_sum *= (10 - digit)

        used_in_digit = [False for _ in range(10)]
        for i, digit in enumerate(digits_n[::-1]):
            if i == 0:
                all_this = digit - 1
            else:
                all_this = 0
                for used in used_in_digit[:digit]:
                    if not used:
                        all_this += 1
            if i == digit_num - 1 and not used_in_digit[digit]:
                all_this += 1
            for j in range(i + 1, digit_num):
                all_this *= (10 - j)
            _sum += all_this
            if not used_in_digit[digit]:
                used_in_digit[digit] = True
            else:
                break

        return _sum

if __name__ == '__main__':
    n = 135
    print(Solution().countSpecialNumbers(n))