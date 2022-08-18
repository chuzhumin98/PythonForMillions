###
# Solution: priority queue, but TLE for python code
# we need to hold for two PQ, one is the maximum PQ for the smaller half part, another is the minimum PQ for the larger half part;
# each time when we push number into one of the PQ, we check for their sizes, when the delta size is larger than 1, we pop the element
# from the larger size one, and then push it into the smaller size one;
# thus, when the total size is odd for the two PQs, the top element of the larger size PQ is the median number!
###


import heapq

N = int(input())
arr = input().split()
arr = [int(_) for _ in arr]

if len(arr) == 0:
    pass
elif len(arr) <= 2:
    print(arr[0])
else:
    arr_hp_low = [-arr[0]]
    arr_hp_high = []
    heapq.heapify(arr_hp_low)
    heapq.heapify(arr_hp_high)
    print(arr[0])
    for i in range(1, N):
        if -heapq.nsmallest(1, arr_hp_low)[0] >= arr[i]:
            heapq.heappush(arr_hp_low, -arr[i])
        else:
            heapq.heappush(arr_hp_high, arr[i])

        if len(arr_hp_low) - len(arr_hp_high) > 1:
            num = heapq.heappop(arr_hp_low)
            heapq.heappush(arr_hp_high, -num)
        elif len(arr_hp_high) - len(arr_hp_low) > 1:
            num = heapq.heappop(arr_hp_high)
            heapq.heappush(arr_hp_low, -num)

        if i % 2 == 0:
            if len(arr_hp_low) > len(arr_hp_high):
                print(-heapq.nsmallest(1, arr_hp_low)[0])
            else:
                print(heapq.nsmallest(1, arr_hp_high)[0])

