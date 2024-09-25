class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans=[]
        ans2=[]
        for i in nums:
            if i % 2==0:
                ans.append(i)
            else : ans2.append(i)    
        return ans + ans2

