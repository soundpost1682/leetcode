class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        cur = float('-inf')
        ans =0
        for i in nums:
            a, b = i-k, i+k
            tmp = max(a, cur)
            if tmp <= b:
                ans +=1
                cur = tmp +1
        return ans
        