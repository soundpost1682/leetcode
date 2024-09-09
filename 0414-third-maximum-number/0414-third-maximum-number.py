class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        tmp =sorted(list(set(nums)))
        if len(tmp) > 2: return tmp[-3]
        return tmp[-1]
