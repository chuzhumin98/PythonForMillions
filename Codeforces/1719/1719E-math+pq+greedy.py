###
# Solution: math + priority queue + greedy
# supplement for tutorial: why "It can be proved that if 𝑐𝑥>𝐹𝑖+1, then it is impossible to represent 𝑐𝑥, as it cannot be represented as the sum of Fibonacci numbers up to 𝐹𝑖 among which there are no neighbors"?
# note that if cx > Fi+1, then the optimal strategy to take cx is Fi + Fi-2 + Fi-4 + ... + F0/1,
# but Fi+1 - (Fi + Fi-2 + Fi-4 + ... + F0/1) = Fi-1 - (Fi-2 + Fi-4 + ... + F0/1) = Fi-3 - (Fi-4 + ... + F0/1) = F1 - F0 or F0 >= 0, so cx > Fi+1 >= Fi + Fi-2 + Fi-4 + ... + F0/1

# following is copyed from the tutorial (https://codeforces.com/blog/entry/106049):
# At the beginning, let's check that the number 𝑛 (the sum of all 𝑐𝑖) is representable as the sum of some prefix of Fibonacci numbers, otherwise we will output the answer NO.
#
# Let's try to type the answer greedily, going from large Fibonacci numbers to smaller ones. For the next Fibonacci number, let's take the letter with the largest number of occurrences in the string from among those that are not equal to the previous letter taken (to avoid the appearance of two adjacent blocks from the same letter, which cannot be). If there are fewer occurrences of this letter than this number, then the answer is NO. Otherwise, we will put the letter on this Fibonacci number and subtract it from the number of occurrences of this letter.If we were able to dial all the Fibonacci numbers, then the answer is YES.
#
# Why does the greedy solution work? Suppose at this step you need to take 𝐹𝑖 (I will say take a number from 𝑐𝑡, this will mean taking 𝐹𝑖 letters 𝑡 from string), let's look at the maximum 𝑐𝑥 now, if it cannot be represented as the sum of Fibonacci numbers up to 𝐹𝑖 among which there are no neighbors, then the answer is no. It can be proved that if 𝑐𝑥>𝐹𝑖+1, then it is impossible to represent 𝑐𝑥.
#
# If there is exactly one number greater than or equal to 𝐹𝑖 at the step, then there is only one option to take a number, so the greedy solution works.
#
# If there are two such numbers and they are equal, then the option to take a number is exactly one, up to the permutation of letters. the greedy solution works again.
#
# If there are 𝑐𝑗≥𝐹𝑖,𝑐𝑥≥𝐹𝑖,𝑗≠𝑥, then we note that the larger of the numbers 𝑐𝑗,𝑐𝑥 will be greater than 𝐹𝑖, if we don't take it, then at the next step this number will be greater than 𝐹𝑖+1 (𝑖 will be 1 less), according to the above proven answer will not be, so, taking the larger of the numbers is always optimal.
#
# The complexity of the solution is 𝑂(𝑘log(𝑛)log(𝑘)).
###

import heapq

FIBNUM = 50
fibs = [1, 1]
for i in range(FIBNUM):
    fibs.append(fibs[-1] + fibs[-2])
fibs_sum = [1]
for num in fibs[1:]:
    fibs_sum.append(num + fibs_sum[-1])
fibs_sum_dict = dict()
for idx, num in enumerate(fibs_sum):
    fibs_sum_dict[num] = idx
# print(fibs[-1])

t = int(input())
for _ in range(t):
    k = int(input())
    arr = input().split()
    arr = [int(i) for i in arr]

    arr_sum = sum(arr)
    if arr_sum not in fibs_sum_dict:
        print("NO")
    else:
        arr_heap = [-i for i in arr]
        heapq.heapify(arr_heap)

        idx = fibs_sum_dict[arr_sum]
        last_value = 0
        success = True
        while True:
            if len(arr_heap) == 0:
                success = False
                break
            value = -heapq.heappop(arr_heap)
            if value < fibs[idx]:
                success = False
                break
            if last_value > 0:
                heapq.heappush(arr_heap, -last_value)
            last_value = value - fibs[idx]
            idx -= 1
            if idx < 0:
                break
        if success:
            print("YES")
        else:
            print("NO")



