###
# Solution:
# no matter suppose x <= y <= z, where x links node v1 and v2, y links node v2 and v3, z links node v3 and v1.
# x, y, z is a permutation of d12, d23, d31; v1, v2, v3 is a permutation of 1, 2, 3
# condition 1: x + y < z, that is impossible, as v1 --- v2 --- v3 is one possible path to link v1, v3,
# and its length equals to x + y, so that x + y <= z
# condition 2: we can construct the subtree to link v1-v2, v2-v3 and v3-v1 as follows:
# v2 ------v1 (left: k, right: x - k, bottom: t
#      |
#      |
#      |
#      v3
# we can get the equations:
# k + t = y
# x - k + t = z
# the ans is t = (y + z - x) / 2, k = (x + y - z) / 2, so the ans exists must satisfy the requirment: x + y - z % 2 == 0
# also, we can find that in the above subtree, the node number = x + t + 1, the ans exists also must satisfy the requirment: x + t + 1 <= n
# Then, if all the three requirments satisfy, we can construct the tree by fulfilling the nodes.
# For example, if n = 7, x = y = 3, y = 4, we can get that k = 1, x - k = 2, t = 2, thus, the subtree node number = x + t + 1 = 6,
# for the one remained node, we can directly link it into node v1 (or 1), that is:
# v2 -  4 -  5 - v1
#       |         |
#       6         7
#       |
#      v3
###

t = int(input())
for _ in range(t):
    arr = input().strip().split()
    n, x, y, z = [int(i) for i in arr]
    v1, v2, v3 = 1, 2, 3
    if x > y:
        v1, v3 = v3, v1
        x, y = y, x
    if y > z:
        v1, v2 = v2, v1
        y, z = z, y
    if x > y:
        v1, v3 = v3, v1
        x, y = y, x
    if x + y < z:
        print("NO")
    elif (x + y - z) % 2 != 0:
        print("NO")
    else:
        # v2 ------v1 (left: k, right: x - k, bottom: t
        #      |
        #      |
        #      |
        #      v3

        lists = []
        t = (y + z - x) // 2
        k = (x + y - z) // 2

        if  x + t + 1 > n:
            print("NO")
        else:
            print("YES")
            last_used_point = 3

            if k == 0:
                pred_point = v2
                for i in range(x):
                    if i != x - 1:
                        last_used_point += 1
                        lists.append([pred_point, last_used_point])
                        pred_point = last_used_point
                    else:
                        lists.append([pred_point, v1])
                pred_point = v2
                for i in range(y):
                    if i != y - 1:
                        last_used_point += 1
                        lists.append([pred_point, last_used_point])
                        pred_point = last_used_point
                    else:
                        lists.append([pred_point, v3])
            else:
                traffic_point = 4
                last_used_point = 4

                pred_point = v2
                for i in range(k):
                    if i != k - 1:
                        last_used_point += 1
                        lists.append([pred_point, last_used_point])
                        pred_point = last_used_point
                    else:
                        lists.append([pred_point, traffic_point])

                pred_point = traffic_point
                for i in range(x - k):
                    if i != x - k - 1:
                        last_used_point += 1
                        lists.append([pred_point, last_used_point])
                        pred_point = last_used_point
                    else:
                        lists.append([pred_point, v1])

                pred_point = traffic_point
                for i in range(t):
                    if i != t - 1:
                        last_used_point += 1
                        lists.append([pred_point, last_used_point])
                        pred_point = last_used_point
                    else:
                        lists.append([pred_point, v3])

            for i in range(last_used_point+1, n+1):
                lists.append([1, i])

            for edge in lists:
                print(edge[0], edge[1])


