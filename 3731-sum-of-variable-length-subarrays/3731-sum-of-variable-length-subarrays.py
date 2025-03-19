class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            a = max(0, i-nums[i])
            ans += sum(nums[a:i+1])
        return ans
        