class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        a=b=0
        for i in nums:
            if i ==0:
                a = max(a,b)
                b = 0
            else:
                b+=1
        return max(a,b)
        

