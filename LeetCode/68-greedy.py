###
# Solution: greedy
# you need to put as more as possible words in each row, and then arrange for the next
# for each line, you need to consider three conditions: the last row, one word row and common row.
###

from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        words_perrow = []
        words_len = []

        words_thisrow = []
        words_thisrow_cnt = -1  # put first word no need one space
        for word in words:
            if len(word) + 1 + words_thisrow_cnt > maxWidth:
                words_perrow.append(words_thisrow)
                words_len.append(words_thisrow_cnt)
                words_thisrow = [word]
                words_thisrow_cnt = len(word)
            else:
                words_thisrow.append(word)
                words_thisrow_cnt += len(word) + 1

        if words_thisrow_cnt > -1:
            words_perrow.append(words_thisrow)
            words_len.append(words_thisrow_cnt)

        spaces_list = ''.join([' ' for _ in range(100)])
        words_perrow_output = []
        for idx, words_thisrow in enumerate(words_perrow):
            if idx == len(words_perrow) - 1:
                line = ' '.join(words_thisrow) + spaces_list[:maxWidth - words_len[idx]]
            else:
                if len(words_thisrow) == 1:
                    line = words_thisrow[0] + spaces_list[:maxWidth - words_len[idx]]
                else:
                    remain_len = maxWidth - words_len[idx]
                    split_num = len(words_thisrow) - 1
                    low_num = remain_len // split_num
                    mod_num = remain_len % split_num
                    for i in range(mod_num):
                        words_thisrow[i] = words_thisrow[i] + spaces_list[:low_num + 1]
                    for i in range(mod_num, split_num):
                        words_thisrow[i] = words_thisrow[i] + spaces_list[:low_num]
                    line = ' '.join(words_thisrow)
            words_perrow_output.append(line)
        return words_perrow_output

if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    print(Solution().fullJustify(words, maxWidth))