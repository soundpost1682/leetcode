class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        answer = total = l = 0
        for hi, n in enumerate(nums):
            total += n
            if total < hi - l:
                total -= nums[l]
                l += 1
            answer = max(answer, hi-l)
        return answer
        

         