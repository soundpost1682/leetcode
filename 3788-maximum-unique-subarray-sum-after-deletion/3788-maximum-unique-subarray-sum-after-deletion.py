class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans=0
        for i in set(nums):
            if i >0: ans+=i
        if ans ==0: return max(nums)
        return ans
        