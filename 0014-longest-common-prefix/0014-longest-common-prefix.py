class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer =''
        s = sorted(strs)
        f = s[0]
        l = s[-1]
        for i in range(min(len(f), len(l))):
            if f[i] != l[i] : return answer
            answer += f[i]
        return answer
        
