class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        return max((len(list(b)) for a, b in groupby(nums) if a==1), default=0)
