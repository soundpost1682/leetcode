class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans=0
        for i in range(len(nums)-1):
            N = bisect_left(nums, lower-nums[i], i+1)
            X = bisect_right(nums, upper-nums[i], i+1)
            ans += N-X
        return abs(ans)

