class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        tmp= {}
        for i in range(len(t)):
            tmp[t[i]] = i
        answer = 0
        for i in range(len(s)):
            answer += abs(i-tmp[s[i]])
        return answer
