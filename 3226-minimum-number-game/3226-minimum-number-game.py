class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ar =[]
        nums.sort()
        for i in range(0, len(nums), 2):
            ar.append(nums[i+1])
            ar.append(nums[i])
        return ar
        