class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        n = min(nums) +k
        m = max(max(nums)-k, n)
        return m -n
        