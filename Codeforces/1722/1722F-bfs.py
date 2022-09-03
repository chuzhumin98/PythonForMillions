###
# Solution: BFS
# a simple bfs problem, we visit for each '*' connection blocks, also to check if each is "L" shape, to answer the question
###
import collections
t = int(input())
s_set = set(['1011', '1110', '1001', '0110', '1-110', '101-1', '0111', '1101'])
for _ in range(t):
    n, m = input().split()
    n, m = int(n), int(m)
    mat = []
    for i in range(n):
        mat.append(list(input().strip()))
    isTrue = True
    for i in range(n):
        for j in range(m):
            if mat[i][j] == '*':
                points = []
                dq = collections.deque()
                mat[i][j] = '.'
                dq.append([i, j])
                while len(dq) > 0:
                    x, y = dq.popleft()
                    points.append([x, y])
                    if x > 0:
                        if mat[x-1][y] == '*':
                            dq.append([x-1, y])
                            mat[x-1][y] = '.'

                        if y > 0:
                            if mat[x-1][y-1] == '*':
                                dq.append([x-1, y-1])
                                mat[x-1][y-1] = '.'
                            if mat[x][y-1] == '*':
                                dq.append([x, y-1])
                                mat[x][y-1] = '.'

                        if y < m-1:
                            if mat[x-1][y+1] == '*':
                                dq.append([x-1, y+1])
                                mat[x-1][y+1] = '.'
                            if mat[x][y+1] == '*':
                                dq.append([x, y+1])
                                mat[x][y+1] = '.'
                    if x < n-1:
                        if mat[x+1][y] == '*':
                            dq.append([x+1, y])
                            mat[x+1][y] = '.'
                        if y > 0:
                            if mat[x+1][y-1] == '*':
                                dq.append([x+1, y-1])
                                mat[x+1][y-1] = '.'
                        if y < m-1:
                            if mat[x+1][y+1] == '*':
                                dq.append([x+1, y+1])
                                mat[x+1][y+1] = '.'
                # print(points)
                if len(points) != 3:
                    print("NO")
                    isTrue = False
                else:
                    s = f'{points[1][0]-points[0][0]}{points[1][1]-points[0][1]}{points[2][0]-points[0][0]}{points[2][1]-points[0][1]}'
                    # print(s)
                    if s not in s_set:
                        print("NO")
                        isTrue = False

                if not isTrue:
                    break
        if not isTrue:
            break
    if isTrue:
        print("YES")



