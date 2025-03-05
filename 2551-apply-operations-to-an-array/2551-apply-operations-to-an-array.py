class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        ans=[]
        tmp=0
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
        for i in nums:
            if i !=0:
                ans.append(i)
            else: tmp+=1
        return ans+[0]*tmp
        