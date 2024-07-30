class Solution:
    def minimumDeletions(self, s: str) -> int:
        tmp = cnt = 0
        for ch in s:
            if ch =='b' :
                cnt += 1
            elif cnt:
                tmp +=1
                cnt -=1
        return tmp
