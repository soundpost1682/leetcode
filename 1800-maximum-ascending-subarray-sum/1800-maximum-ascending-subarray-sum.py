class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        a, b = 0, nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                b += nums[i]
            else:
                a = max(a,b)
                b = nums[i]
        return max(a,b)

