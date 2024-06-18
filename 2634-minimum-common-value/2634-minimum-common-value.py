class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        s = set(nums1).intersection(set(nums2))
        return min(s) if len(s) >0 else -1
        