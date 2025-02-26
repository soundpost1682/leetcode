class Solution:
    def finalString(self, s: str) -> str:
        ans=s[0]
        for i in range(1, len(s)):
            if s[i] == 'i':
                ans = ans[::-1]
            else: ans = ans + s[i]
        return ans
        