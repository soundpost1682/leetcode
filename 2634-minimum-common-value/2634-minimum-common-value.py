class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        l, r = 0,0
        while l < l1 and r < l2:
            a = nums1[l]
            b = nums2[r]
            if a == b: return b
            elif a > b: r += 1
            else : l += 1
        return -1

