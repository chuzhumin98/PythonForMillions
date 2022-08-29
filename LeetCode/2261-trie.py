###
# Solution: Trie
# the difficulty is how to store the already record sublist
# one method is hashmap, we can join all the used number into a string
# we use another method: Trie, to flow for the node change
###

from typing import List
class TrieNode:
    def __init__(self):
        self.Next = dict()  # num -> TrieNode


class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        _sum = 0
        nums_pd = [True if num % p == 0 else False for num in nums]
        root = TrieNode()
        for i in range(len(nums)):
            cnt_pd = 0
            node = root
            for j in range(i, len(nums)):
                if nums_pd[j]:
                    cnt_pd += 1
                if cnt_pd > k:
                    break
                if nums[j] not in node.Next:
                    node.Next[nums[j]] = TrieNode()
                    node = node.Next[nums[j]]
                    node.Next[-1] = TrieNode()
                    _sum += 1
                else:
                    node = node.Next[nums[j]]
                    if -1 not in node.Next:
                        _sum += 1
                        node.Next[-1] = TrieNode()
        return _sum

