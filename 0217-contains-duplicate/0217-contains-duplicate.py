class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        N = sorted(nums, reverse=True)
        for i in range(1, len(nums)):
            if N[i] == N[i-1]: return True
        return False

