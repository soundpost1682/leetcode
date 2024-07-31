class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        ar =[]
        while nums:
            ar.append(nums[1])
            ar.append(nums[0])
            nums= nums[2:]
        return ar

