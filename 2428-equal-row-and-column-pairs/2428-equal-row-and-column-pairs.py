class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        tmp =0
        cnt = Counter(tuple(r) for r in grid)
        for i in zip(*grid):
            tmp += cnt[i]
        return tmp
        