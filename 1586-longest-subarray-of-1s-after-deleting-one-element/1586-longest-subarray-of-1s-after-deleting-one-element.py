class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        total = pre = cur = 0
        for i in nums:
            if i :
                cur += 1
                total = max(total, pre + cur)
            else: 
                pre , cur = cur, 0
        return total - (total == len(nums))
        