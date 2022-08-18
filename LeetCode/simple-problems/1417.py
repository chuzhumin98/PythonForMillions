class Solution:
    def reformat(self, s: str) -> str:
        letters_list = []
        digits_list = []
        for char in s:
            if ord(char) >= ord('0') and ord(char) <= ord('9'):
                digits_list.append(char)
            else:
                letters_list.append(char)
        if abs(len(digits_list) - len(letters_list)) <= 1:
            total_s = ''
            if len(digits_list) >= len(letters_list):
                for i in range(len(s)):
                    total_s += digits_list[i // 2] if i % 2 == 0 else letters_list[i // 2]
            else:
                for i in range(len(s)):
                    total_s += letters_list[i // 2] if i % 2 == 0 else digits_list[i // 2]
        else:
            total_s = ''
        return total_s