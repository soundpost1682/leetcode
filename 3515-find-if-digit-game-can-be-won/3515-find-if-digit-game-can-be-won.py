class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a,b=0,0
        for i in nums:
            if i > 9:
                a += i
            elif i < 10 :
                b += i
        if a > b or a < b : return True
        else: return False
        

