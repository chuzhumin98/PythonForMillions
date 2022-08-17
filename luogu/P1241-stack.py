###
# Solution: stack
# first round visit each char of the string, push all ( and [ into stack, for ] and ) if can be paired with the stack top element,
# then pop this element from stack, else record it, when second visit the string, correct it to be [] or ()
# as for the all final remained stack elements, also correct it in the second visit
###

probs_s = []

s = input().strip()
stack = []
for i, char in enumerate(s):
    if char in ['(', '[']:
        stack.append([char, i])
    elif len(stack) == 0:
        probs_s.append(i)
    elif char == ')' and stack[-1][0] == '(':
        stack.pop()
    elif char == ']' and stack[-1][0] == '[':
        stack.pop()
    else:
        probs_s.append(i)

for _, idx in stack:
    probs_s.append(idx)

probs_s = set(probs_s)
s_out = ''
for i, char in enumerate(s):
    if i not in probs_s:
        s_out += char
    else:
        if char in ['(', ')']:
            s_out += '()'
        else:
            s_out += '[]'

print(s_out)