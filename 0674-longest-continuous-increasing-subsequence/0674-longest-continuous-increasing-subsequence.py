class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        answer, cnt =0,0
        for i in range(len(nums)):
            if nums[i-1] >= nums[i] : cnt = i
            answer = max(answer, i-cnt+1)
        return answer
