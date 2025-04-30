class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans =0
        for i in nums:
            if 9 < i < 100 or 999 < i < 10000 or i==100000:
                ans+=1
        return ans

