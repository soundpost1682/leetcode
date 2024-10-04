class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        tmp = set(nums)
        tmp2 = []
        for i in range(1, len(nums)+1):
            if i not in tmp:
                tmp2.append(i)
        return tmp2
