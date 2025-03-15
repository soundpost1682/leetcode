class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        a,b,c=1,1,1
        tmp = nums.pop(0)
        for i in nums:
            a = a*(i > tmp) +1
            b = b*(i < tmp) +1
            tmp = i
            c = max(a,b,c)
        return c
        