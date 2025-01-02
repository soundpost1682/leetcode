class Solution:
    def maxScore(self, s: str) -> int:
        maxscore = left = 0
        right = s.count('1')
        for i in range(len(s)-1):
            left += s[i] == '0'
            right -= s[i] == '1'
            maxscore = max(maxscore, left + right)
        return maxscore
