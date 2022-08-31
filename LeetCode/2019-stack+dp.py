###
# Solution: stack + dp
# for the right answer, we hold with a stack, when the oper is '*', we pop the pred val and turn to the next val, mulitply them
# and then push it into stack; else we directly push into stack; in the second round, we add with every value in the stack to gain
# the correct answer;
# for the candidates answers, we use range dp to store, let f(m, n) be the set of all possible answer with the [m, n] values in
# any oper order, then f(m, n) = Union_{k| m <= k < n} {f(m, k) + f(k+1, n)}
###

from typing import List
class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        n_num = (len(s) + 1) // 2
        stack = []
        for char in s:
            if char == '+' or char == '*':
                stack.append(char)
            else:
                val = int(char)
                if len(stack) > 0 and stack[-1] == '*':
                    stack.pop()
                    val2 = stack.pop()
                    stack.append(val * val2)
                else:
                    stack.append(val)
        while len(stack) > 1:
            val, _, val2 = stack.pop(), stack.pop(), stack.pop()
            stack.append(val + val2)
        right_ans = stack[0]

        potential_list = [[set() for _ in range(n_num)] for __ in
                          range(n_num)]  # i, j: the potential value for the expr value i to j
        for i in range(n_num):
            potential_list[i][i].add(int(s[i * 2]))
        for i in range(1, n_num):
            for j in range(n_num - i):
                # p[j][j+i]
                for k in range(j, j + i):
                    if s[k * 2 + 1] == '+':
                        for val1 in potential_list[j][k]:
                            for val2 in potential_list[k + 1][j + i]:
                                val = val1 + val2
                                if val <= 1000:
                                    potential_list[j][j + i].add(val)
                    else:
                        for val1 in potential_list[j][k]:
                            for val2 in potential_list[k + 1][j + i]:
                                val = val1 * val2
                                if val <= 1000:
                                    potential_list[j][j + i].add(val)
        answers_set = potential_list[0][n_num - 1]

        _sum = 0
        for ans in answers:
            if ans in answers_set:
                _sum += 2
                if ans == right_ans:
                    _sum += 3
        return _sum

