class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for a,b in enumerate(nums):
            if b >= target:
                return a
        return len(nums)
        
