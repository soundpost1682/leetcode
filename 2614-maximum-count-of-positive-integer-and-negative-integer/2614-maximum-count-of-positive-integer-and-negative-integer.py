class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        po,ne=0,0
        for i in nums:
            if i < 0:
                ne+=1
            if i >= 1:
                po+=1
        return max(po,ne)
        