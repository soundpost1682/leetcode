class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        tmp = set()
        for i in nums:
            if i in tmp: tmp.remove(i)
            else : tmp.add(i)
        return not tmp
