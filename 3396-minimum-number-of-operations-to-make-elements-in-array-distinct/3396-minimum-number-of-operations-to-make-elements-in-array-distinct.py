class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt=0
        while len(nums) > len(set(nums)):
            nums = nums[3:]
            cnt+=1
        return cnt
        