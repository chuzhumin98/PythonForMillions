###
# Solution: dfs
# we use dfs to enumerate each valid path, also attention! we need to record the last direction, current direction can
# not be the same as the last one!
# preprocess: the reachable and direction relation between cows and start point
###

def dfs(links_matrix, axis_required, current_idx, remain_set, _sum, pred_dir):
    if len(remain_set) == 0:
        if current_idx in axis_required and pred_dir != axis_required[current_idx]:
            _sum[0] += 1
        return
    for idx, cur_dir in links_matrix[current_idx]:
        if idx in remain_set and cur_dir != pred_dir:
            remain_set.remove(idx)
            dfs(links_matrix, axis_required, idx, remain_set, _sum, cur_dir)
            remain_set.add(idx)

n = int(input())
points = []
for _ in range(n):
    x, y = input().split()
    x, y = int(x), int(y)
    points.append([x, y])

sameposis = dict()
for x, y in points:
    sameposis[x * 10000 + y] = sameposis.get(x * 10000 + y, 0) + 1

mod = 1
for v in sameposis.values():
    mod *= v

_sum = [0]

axis_required = dict()
for idx, point in enumerate(points):
    if point[0] == 0:
        axis_required[idx] = 0 if point[1] < 0 else 2
    elif point[1] == 0:
        axis_required[idx] = 1 if point[0] < 0 else 3

links_matrix = []
for idx, point in enumerate(points):
    links_this = []
    for _idx, _point in enumerate(points):
        if idx != _idx:
            if _point[0] == point[0]:
                links_this.append([_idx, 0 if _point[1] >= point[1] else 2]) # N 0, S 2
            elif _point[1] == point[1]:
                links_this.append([_idx, 1 if _point[0] >= point[0] else 3])  # E 1, W 3

    links_matrix.append(links_this)

# print(axis_required, links_matrix)

remain_set = set(list(range(n)))
for sidx in axis_required:
    remain_set.remove(sidx)
    dfs(links_matrix, axis_required, sidx, remain_set, _sum, (axis_required[sidx] + 2) % 4)
    remain_set.add(sidx)

print(_sum[0] // mod)

