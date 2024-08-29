class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        M =max(nums)
        for i in range(M+1, M+k):
            M +=i
        return M
        