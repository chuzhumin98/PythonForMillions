###
# Solution: BFS
# a simple bfs problem, the state contains the position (x, y) and current direction r, next we just use bfs
# to find the min path from start to end
###

import collections
def go_direction(x, y, step, direction):
    if direction == 0:
        return x + step, y
    elif direction == 1:
        return x - step, y
    elif direction == 2:
        return x, y + step
    elif direction == 3:
        return x, y - step
    elif direction == 4:
        return x + step, y + step
    elif direction == 5:
        return x - step, y - step
    elif direction == 6:
        return x + step, y - step
    else:
        return x - step, y + step


N, M = input().split()
N, M = int(N), int(M)

matrix = []
for i in range(M):
    arr = input().split()
    arr = [int(_) for _ in arr]
    matrix.append(arr)

min_steps = [[[-1 for _ in range(8)] for __ in range(N)] for ___ in range(M)]

for i in range(8):
    min_steps[0][0][i] = 0

dq = collections.deque()
dq.append([0, 0, -1, 0]) # x, y, pred_dir

complete = False
while True:
    if len(dq) == 0:
        break
    x, y, pred_dir, min_step = dq.popleft()
    step = matrix[x][y]
    min_step += 1
    for dir_this in range(8):
        if pred_dir != dir_this:
            xnew, ynew = go_direction(x, y, step, dir_this)
            if xnew >= 0 and ynew >= 0 and xnew < M and ynew < N:
                if min_steps[xnew][ynew][dir_this] == -1:
                    if xnew == M-1 and ynew == N-1:
                        print(min_step)
                        complete = True
                        break

                    min_steps[xnew][ynew][dir_this] = min_step
                    dq.append([xnew, ynew, dir_this, min_step])

    if complete:
        break

if not complete:
    print('NEVER')