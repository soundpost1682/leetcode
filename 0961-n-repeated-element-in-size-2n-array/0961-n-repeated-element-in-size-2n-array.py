class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        tmp =[]
        for i in nums:
            if i in tmp : return i
            else : tmp.append(i)
        