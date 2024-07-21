class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saw = {}
        for i, v in enumerate(nums):
            remain = target - nums[i]

            if remain in saw:
                return [i, saw[remain]]
            else: saw[v] = i
            
