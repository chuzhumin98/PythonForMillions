###
# Solution: stack
# we hold with two stacks: one stores with operations ( '(', '+', '-' ), another stores with numbers,
# in each time, we calculate for the previous numbers and operations as much as possible (isolate with '(' unless meet ')' )
# as for the ...-(...) or -... conditions, we detect them and push extra 0 into nums stack
###
class Solution:
    def calc(self):
        if len(self.opers) > 0 and self.opers[-1] != '(':
            # print(self.opers, self.nums)
            oper = self.opers.pop()
            num2 = self.nums.pop()
            num1 = self.nums.pop()
            if oper == '+':
                self.nums.append(num1 + num2)
            else:
                self.nums.append(num1 - num2)

    def calculate(self, s: str) -> int:
        self.nums, self.opers = [], []
        s = s.replace(" ", "")
        cur_num = 0
        is_num_pred = False
        for i, char in enumerate(s):
            if char == '(':
                is_num_pred = False
                self.opers.append(char)
            elif char == ')':
                if is_num_pred:
                    is_num_pred = False
                    self.nums.append(cur_num)
                    cur_num = 0
                while True:
                    if self.opers[-1] == '(':
                        self.opers.pop()
                        break
                    else:
                        self.calc()
            elif char in ['+', '-']:
                if is_num_pred:
                    is_num_pred = False
                    self.nums.append(cur_num)
                    cur_num = 0
                elif (i > 0 and s[i - 1] == '(') or i == 0:
                    self.nums.append(0)
                self.calc()
                self.opers.append(char)
            else:
                cur_num = cur_num * 10 + int(char)
                is_num_pred = True
        if is_num_pred:
            self.nums.append(cur_num)
        self.calc()
        return self.nums[0]
