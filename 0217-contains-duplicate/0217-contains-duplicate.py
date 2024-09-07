class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        saw=set(nums)
        if len(nums) != len(saw):
            return True
        return False
        