class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        answer=0
        for i in range(0, len(nums)):
            v = bin(i)[2:]
            result = str(v).count('1')
            if result == k:
                answer += nums[i]
        return answer
            