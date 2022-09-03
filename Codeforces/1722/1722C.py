###
# simple problem, no need to say
###
t = int(input())
for _ in range(t):
    n = int(input())
    ss = []
    for i in range(3):
        ss.append(input().strip().split())
    cnts = dict()
    for items in ss:
        for item in items:
            cnts[item] = cnts.get(item, 0) + 1
    scores = []
    s_list = [0, 3, 1, 0]
    for items in ss:
        _s = 0
        for s in items:
            _s += s_list[cnts[s]]
        scores.append(_s)
    print(' '.join([str(i) for i in scores]))
