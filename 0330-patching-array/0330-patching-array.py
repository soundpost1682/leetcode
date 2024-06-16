class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cnt, i, mis= 0,0,1
        while mis <= n:
            if i < len(nums) and nums[i] <= mis:
                mis += nums[i]
                i += 1
            else:
                mis += mis
                cnt += 1
        return cnt
        