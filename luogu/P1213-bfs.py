###
# Solution: BFS + State Compress, TLE with python code
# each clock has 4 status: 1 (3:00), 2 (6:00), 3 (9:00), 0 (0:00)
# each step make some clocks s to be (s+1)%4, final goal is to be 000000000
# We use BFS to search with both the step num and the strategy in increasing order
###

import collections
final_status = '000000000'

actions = [[0, 1, 3, 4], [0, 1, 2], [1, 2, 4, 5], [0, 3, 6],
           [1, 3, 4, 5, 7], [2, 5, 8], [3, 4, 6, 7],
           [6, 7, 8], [4, 5, 7, 8]]

status = []
for i in range(3):
    arr = input().split()
    arr = [int(_)  for _ in arr]
    for num in arr:
        status.append((num//3)%4)

status_steps = dict()
s0 = ''.join([str(_) for _ in status])
status_steps[s0] = [0, 0, ''] # step num, action type, pred status
if s0 == final_status:
    print('')
else:
    dq = collections.deque()
    dq.append(s0)
    while True:
        if len(dq) == 0:
            break
        st = dq.popleft()
        step_num, _, _ = status_steps[st]
        for i, step in enumerate(actions):
            stat = [int(char) for char in st]
            for idx in step:
                stat[idx] = (stat[idx] + 1) % 4
            snew = ''.join([str(_) for _ in stat])
            if snew not in status_steps:
                status_steps[snew] = [step_num + 1, i+1, st]
                dq.append(snew)
        if final_status in status_steps:
            cur_status = final_status
            pathes = []
            while True:
                _, type, cur_status = status_steps[cur_status]
                if cur_status == '':
                    break
                pathes.append(type)

            print(' '.join([str(_) for _ in pathes[::-1]]))
            break

