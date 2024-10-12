class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ans =k
        for i in nums:
            if i == 0: ans+=1
            else: 
                if k > ans: return False
                ans=0
        return True
        