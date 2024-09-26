class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=b=0
        for i in range(len(nums)):
            if nums[i] == 1:
                a+=1
            else:
                b = max(a, b)
                a=0
        return max(a,b)
