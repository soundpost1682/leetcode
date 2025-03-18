class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        tmp =[]
        for i in nums:
            if i%2==0: tmp.append(0)
            else:tmp.append(1)
        return sorted(tmp)
        