class Solution:
    def ten2binary(self, n):
        if n == 0:
            return '0'
        s = ''
        while n > 0:
            s += str(n % 2)
            n //= 2
        return s[::-1]

    def binary2ten(self, s):
        n = 0
        for char in s:
            if char == '1':
                n = n * 2 + 1
            else:
                n = n * 2
        return n

    def addBinary(self, a: str, b: str) -> str:
        return self.ten2binary(self.binary2ten(a) + self.binary2ten(b))