class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a = b = 0
        for i in s:
            if i == '(': a+=1
            else :
                if a : a-=1
                else: b +=1
        return a + b
        