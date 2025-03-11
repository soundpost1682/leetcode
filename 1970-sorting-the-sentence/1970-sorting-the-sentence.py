class Solution:
    def sortSentence(self, s: str) -> str:
        tmp = [i[-1] + i[:-1] for i in s.split()]
        tmp.sort()
        ans = ''
        for i in tmp:
            ans += i[1:] + ' '
        return ans[:-1]
