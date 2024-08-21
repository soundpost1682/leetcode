class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        FB=SB=0
        FS=SS=float('inf')
        for num in nums:
            if num < FS:
                SS, FS = FS, num
            elif num < SS:
                SS = num
            
            if num > FB:
                SB, FB = FB, num
            elif num > SB:
                SB = num
        return FB * SB - FS * SS

