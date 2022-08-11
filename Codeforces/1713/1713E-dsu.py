###
# Solution: Disjoint Set Union (DSU), TLE with python, but AC with C++
# we can find change k twice equals to no change, so for each k, we have two states: change k once (co) or nochange (nc)
# for any pair A_ij and A_ji, we only concern i != j condition, then
# we change the pair <==> i and j have the different state (co v.s. nc);
# we unchange the pair <==> i and j have the same state
# we can change or unchange the pair <==> i and j have no constraint
# for the lexicographically smallest matrix, we need to concern any (i, j) pair (i > j) from the i * n + j priority (from small to large)
# thus we can use this criteria to build a DSU, also to store the stage: whether this node's state equals to its parent node
###

def get_parent(union_set, node):
    if union_set[node][0] == node:
        return union_set[node]
    else:
        parent, flag = union_set[node]
        root, flag_p = get_parent(union_set, parent)
        flag_new = (flag + flag_p) % 2
        union_set[node] = [root, flag_new]
        return union_set[node]

def merge(union_set, nodeA, nodeB, flag):
    parA, flagA = get_parent(union_set, nodeA)
    parB, flagB = get_parent(union_set, nodeB)
    if parA != parB:
        union_set[parB] = [parA, (flag+flagA+flagB)%2]

t = int(input())
for _ in range(t):
    n = int(input())
    matrix = []
    for i in range(n):
        arr = input().split()
        arr = [int(__) for __ in arr]
        matrix.append(arr)

    union_set = [[i, 0] for i in range(n)] # 0: same with root, 1: unsame with root
    for i in range(n):
        for j in range(i+1, n):
            if matrix[i][j] < matrix[j][i]:
                merge(union_set, i, j, 0)
            elif matrix[i][j] > matrix[j][i]:
                merge(union_set, i, j, 1)
            else:
                pass

    for i in range(n):
        __, flag = get_parent(union_set, i)
        if flag == 1: # change for all flag == 1
            for j in range(n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        print(' '.join([str(__) for __ in matrix[i]]))
