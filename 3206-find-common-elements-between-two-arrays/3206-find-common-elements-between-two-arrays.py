class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        a,b = 0,0
        for n1 in nums1:
            if n1 in s2:
                a+=1
        for n2 in nums2:
            if n2 in s1:
                b+=1
        return [a, b]