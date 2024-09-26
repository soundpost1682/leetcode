class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=b=0
        for i in nums:
            a = a * i+i
            b = max(b, a)
        return b
        