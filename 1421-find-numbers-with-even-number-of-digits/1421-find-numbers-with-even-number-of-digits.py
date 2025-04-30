class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum([i%2==0 for i in map(len,map(str,nums))])
        