class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        answer= {}
        for i in range(len(t)):
            answer[t[i]] = i
        tmp = 0
        for i in range(len(s)):
            tmp += abs(i-answer[s[i]])
        return tmp
        