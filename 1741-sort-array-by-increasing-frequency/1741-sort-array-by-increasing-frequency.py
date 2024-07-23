class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        a = sorted(nums, reverse=True)
        b = sorted(a, key = nums.count)
        return b
        

