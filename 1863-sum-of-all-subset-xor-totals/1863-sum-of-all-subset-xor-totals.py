class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def tmp(a, b):
            if a == len(nums):
                return b
            tmp2 = tmp(a + 1, b ^ nums[a])
            tmp3 = tmp(a + 1, b)
            return tmp2 + tmp3
        return tmp(0,0)
        