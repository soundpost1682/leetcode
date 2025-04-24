class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total = len(set(nums))
        cnt=0
        for i in range(len(nums)):
            saw=set()
            for j in range(i, len(nums)):
                saw.add(nums[j])
                if len(saw) == total:
                    cnt += len(nums) - j
                    break
        return cnt
        