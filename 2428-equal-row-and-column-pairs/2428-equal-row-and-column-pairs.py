class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        tmp = Counter(zip(*grid))
        G = Counter(map(tuple, grid))
        return sum(tmp[i] * G[i] for i in tmp)
