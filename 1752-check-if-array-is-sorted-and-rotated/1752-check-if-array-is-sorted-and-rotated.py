class Solution:
    def check(self, nums: List[int]) -> bool:
        l = len(nums)
        tmp=0
        for i in range(1, l):
            if nums[i] < nums[i-1]:
                tmp +=1
                if tmp > 1: return False
        if nums[0] < nums[l-1]:
            tmp +=1
        return tmp <=1
        
            
            