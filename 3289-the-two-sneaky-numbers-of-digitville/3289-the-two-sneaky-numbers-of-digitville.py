class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        v = set()
        ans =[]
        for i in nums:
            if i not in v: v.add(i)
            else: ans.append(i)
        return ans
        

