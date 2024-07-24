class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        tmp =0
        for i in nums:
            if i % 3:
                tmp += 1
        return tmp

