class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = tmp = 0
        for i in s:
            if i == '(': ans+=1
            else :
                if ans : ans-=1
                else: tmp +=1
        return ans + tmp

