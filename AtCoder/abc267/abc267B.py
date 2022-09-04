s = input().strip()
s = list(s)

if s[0] != '0':
    print('No')
else:
    knocks = []
    unknocks = []
    arrs = [[6], [3], [7, 1], [4, 0], [8, 2], [5], [9]]
    for i, items in enumerate(arrs):
        kn, unkn = True, False
        for item in items:
            if s[item] == '1':
                kn = False
                unkn = True
                break
        if kn:
            knocks.append(i)
        if unkn:
            unknocks.append(i)

    if len(knocks) < 1 or len(unknocks) < 2:
        print("No")
    else:
        unkmax, unkmin = max(unknocks), min(unknocks)
        is_can = False
        for kidx in knocks:
            if kidx < unkmax and kidx > unkmin:
                is_can = True
                break
        if is_can:
            print("Yes")
        else:
            print("No")