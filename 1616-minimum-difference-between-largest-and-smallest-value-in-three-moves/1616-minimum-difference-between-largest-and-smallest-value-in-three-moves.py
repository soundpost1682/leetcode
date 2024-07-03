class Solution:
    def minDifference(self, nums: List[int]) -> int:
        a = len(nums)
        if a <= 4: return 0
        nums.sort()
        m = min(
            nums[a-1] - nums[3],
            nums[a-2] - nums[2],
            nums[a-3] - nums[1],
            nums[a-4] - nums[0]
        )
        return m
        