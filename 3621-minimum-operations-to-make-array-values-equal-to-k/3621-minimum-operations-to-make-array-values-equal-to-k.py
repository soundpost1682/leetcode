class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        H =0
        tmp=101
        for i in nums:
            H |= 1<<i
            tmp = min(i, tmp)
        if tmp < k: return -1
        ans = H.bit_count()
        return ans-1 if tmp == k else ans
