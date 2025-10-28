class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        tmp = list(accumulate(nums, initial=0))
        a,b,c = len(nums), 0, tmp[-1]

        for i,j in zip(nums, tmp):
            j *= 2

            if i : continue
            if c == j : b +=2
            if abs(c - j) == 1 : b +=1
        
        return b
        