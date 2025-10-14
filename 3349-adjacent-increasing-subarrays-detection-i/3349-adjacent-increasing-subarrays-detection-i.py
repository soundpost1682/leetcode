class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        saw = k-1
        if saw ==0: return True
        for i in range(k+1, len(nums)):
            if nums[i] > nums[i-1] and nums[i-k] > nums[i-k-1]:
                saw -=1
            else : saw = k-1
            if saw ==0: return True
        return False
        