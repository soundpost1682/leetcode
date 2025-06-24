class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        l = len(nums)
        ans =[]
        b =0
        for i in range(l):
            if nums[i] == key:
                a = max(b, i-k)
                b = min(l, i+k+1)
                ans.extend(range(a,b))
        return ans
        
        