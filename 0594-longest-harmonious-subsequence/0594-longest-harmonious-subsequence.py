class Solution:
    def findLHS(self, nums: List[int]) -> int:
        tmp = Counter(nums)
        res =0
        for i in tmp:
            if i+1 in tmp:
                res = max(res, tmp[i] + tmp[i+1])
        return res
        