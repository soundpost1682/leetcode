class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        t =sorted(nums)
        n,m = 0,0
        for i in t:
            n = max(n, i)
            m += n - i
            n += 1
        return m
        