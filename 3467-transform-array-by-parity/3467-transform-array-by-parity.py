class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        return sorted([1 if i%2 else 0 for i in nums])

