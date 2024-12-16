class Solution:
    def getFinalState(self, nums: List[int], k: int, m: int) -> List[int]:
        for i in range(k):
            id = 0
            ans= nums[0]
            for i in range(1, len(nums)):
                if nums[i] < ans:
                    ans = nums[i]
                    id = i
            nums[id] *= m
        return nums
        