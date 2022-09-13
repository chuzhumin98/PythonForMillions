class Solution:
    def shift(self, char, n):
        return chr(ord(char) + n)

    def replaceDigits(self, s: str) -> str:
        s_out = ''
        for i, char in enumerate(s):
            if i % 2 == 0:
                s_out += char
            else:
                s_out += self.shift(s[i-1], int(char))
        return s_out