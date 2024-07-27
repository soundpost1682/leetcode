class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = []
        ind = 0
        while ind < len(nums):
            beg = nums[ind]
            while ind+1 < len(nums) and nums[ind+1] == nums[ind] +1:
                ind += 1
            last = nums[ind]

            if beg == last:
                out.append(str(beg))
            else : 
                out.append(str(beg) + '->' + str(last))
            ind += 1
        return out

