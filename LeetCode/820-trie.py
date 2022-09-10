###
# Solution: trie
# a trie template problem, no need to say more
###
from typing import List

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]


class Solution:
    def letter2index(self, char):
        return ord(char) - ord('a')

    def dfs(self, node):
        cnt_notnone = 0
        self.path.append(node)
        for nodeN in node.children:
            if nodeN is not None:
                self.dfs(nodeN)
                cnt_notnone += 1

        if cnt_notnone == 0:
            self.ans += len(self.path)

        self.path.pop()

    def minimumLengthEncoding(self, words: List[str]) -> int:
        root = TrieNode()
        for word in words:
            node = root
            for char in word[::-1]:
                idx = self.letter2index(char)
                if node.children[idx] is None:
                    node.children[idx] = TrieNode()
                node = node.children[idx]

        self.path = []
        self.ans = 0
        self.dfs(root)
        return self.ans



