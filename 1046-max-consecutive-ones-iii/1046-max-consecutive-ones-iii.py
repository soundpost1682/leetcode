class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        L=R=0
        for i in range(len(nums)):
            if nums[i] == 0:
                k -= 1
            if k < 0:
                if nums[L] == 0:
                    k+=1
                L+=1
        return i - L + 1

            