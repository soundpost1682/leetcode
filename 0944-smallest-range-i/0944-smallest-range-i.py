class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        n = min(nums)
        m = max(nums)
        return max(0, (m-k) - (n+k))
        
