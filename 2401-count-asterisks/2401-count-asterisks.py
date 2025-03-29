class Solution:
    def countAsterisks(self, s: str) -> int:
        tmp,ans=0,0
        for i in range(len(s)):
            if s[i] == '|':
                tmp+=1
            if tmp%2==0:
                if s[i] == '*':
                    ans+=1
        return ans
        