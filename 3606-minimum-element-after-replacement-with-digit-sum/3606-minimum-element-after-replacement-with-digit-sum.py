class Solution:
    def minElement(self, nums: List[int]) -> int:
        tmp = lambda n : sum(int(j) for j in str(n))
        return min(map(tmp, nums))

