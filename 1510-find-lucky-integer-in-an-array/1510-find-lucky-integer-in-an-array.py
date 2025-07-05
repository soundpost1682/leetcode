class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max((i for i,j in Counter(arr).items() if i==j), default=-1)
