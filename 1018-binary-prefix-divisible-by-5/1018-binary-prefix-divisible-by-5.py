class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans, tmp = [], 0
        for i in nums:
            tmp = (tmp*2 + i) %5
            ans.append(tmp==0)
        return ans
        