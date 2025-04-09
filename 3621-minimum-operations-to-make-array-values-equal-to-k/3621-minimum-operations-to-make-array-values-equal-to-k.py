class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):return -1
        saw= set(nums)
        tmp = len(saw)
        if k in saw: return tmp-1
        else: return tmp
