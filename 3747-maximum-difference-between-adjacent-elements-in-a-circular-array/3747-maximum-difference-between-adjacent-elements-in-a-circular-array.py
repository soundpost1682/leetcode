class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        t = len(nums)
        tmp_mx = abs(nums[0] - nums[-1])
        for i in range(len(nums)-1):
            tmp_mx = max(tmp_mx, abs(nums[i] - nums[i+1]))
        return tmp_mx
        

