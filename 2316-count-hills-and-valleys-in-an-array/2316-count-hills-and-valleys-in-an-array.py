class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        tmp =[i for i,v in groupby(nums)]
        return sum(l>m<r or l<m>r for l,m,r in zip(tmp,tmp[1:],tmp[2:]))
        
