class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = [0 for _ in range(len(blocks) + 1)]
        _min = len(blocks)
        for i, block in enumerate(blocks):
            if block == 'W':
                whites[i+1] = whites[i] + 1
            else:
                whites[i+1] = whites[i]
        for i in range(len(blocks) - k + 1):
            _min = min(_min, whites[i+k] - whites[i])
        return _min