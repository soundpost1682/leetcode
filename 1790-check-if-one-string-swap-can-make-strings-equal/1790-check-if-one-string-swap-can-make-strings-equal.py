class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:return True
        tmp= [i for i in range(len(s1)) if s1[i] != s2[i]]
        return len(tmp)==2 and s1[tmp[0]] == s2[tmp[1]] and s1[tmp[1]] == s2[tmp[0]]
        