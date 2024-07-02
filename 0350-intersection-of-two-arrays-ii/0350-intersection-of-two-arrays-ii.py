class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = collections.Counter(nums1)
        b = collections.Counter(nums2)
        tmp=[]
        for i in a.keys() & b.keys():
            tmp.extend([i] * min(a[i], b[i]))
        return tmp
