class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(i < k for i in nums):
            return -1
        
        saw=set()
        for i in nums:
            if i > k: saw.add(i)
        return len(saw)
        