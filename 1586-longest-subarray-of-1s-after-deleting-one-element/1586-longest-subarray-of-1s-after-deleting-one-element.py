class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        L = zero = answer = 0
        for R in range(len(nums)):
            if nums[R] == 0:
                zero += 1
            while zero > 1:
                if nums[L] ==0:
                    zero -= 1
                L += 1
            answer = max(answer, R - L + 1 - zero)
        return answer -1 if answer == len(nums) else answer
