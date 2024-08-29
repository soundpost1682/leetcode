class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        m = nums[0]
        for i in nums:
            if i > m: m=i
        answer =0
        for i in range(0, k):
            answer += m
            m +=1
        return answer
        
