class Solution:
    def countAsterisks(self, s: str) -> int:
        ans=0
        T=True
        for i in s:
            if T and i == '*':
                ans+=1
            if i == '|':
                T = not T
        return ans
        