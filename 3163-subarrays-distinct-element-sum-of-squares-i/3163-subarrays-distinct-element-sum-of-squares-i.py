class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        tmp =[]
        for i in range(len(nums)):
            for j in range(i, len(nums)+1):
                tmp.append(len(set(nums[i:j])) **2)
        return sum(tmp)
        