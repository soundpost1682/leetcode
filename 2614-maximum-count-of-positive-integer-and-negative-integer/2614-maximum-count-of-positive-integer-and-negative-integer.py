class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        ne = bisect_left(nums, 0)
        po = len(nums) - bisect_right(nums, 0)
        return max(po,ne)
        