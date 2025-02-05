class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        tmp = [[a,b] for a,b in zip(s1,s2) if a!=b]
        return not tmp or len(tmp)==2 and tmp[0][::-1] == tmp[1]
