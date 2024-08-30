class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        a=sorted(nums1)
        b=sorted(nums2)
        return min(b) - min(a)
        
