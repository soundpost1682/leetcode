class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        tmp = [0] * n
        for i, j in roads:
            tmp[i] += 1
            tmp[j] += 1
        tmp.sort()
        s=0
        for i in range(len(tmp)):
            s += tmp[i] * (i+1)
        return s
