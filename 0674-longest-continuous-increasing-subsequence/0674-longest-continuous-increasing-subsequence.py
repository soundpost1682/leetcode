class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        cnt , ans = 1,0
        for i in range(len(nums)):
            for j in range(i, len(nums)-1):
                if nums[j] < nums[j+1] :
                    cnt+=1
                else: break
            
            ans=max(cnt, ans)
            cnt=1
        return ans
