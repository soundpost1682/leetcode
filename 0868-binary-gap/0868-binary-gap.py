class Solution:
    def binaryGap(self, n: int) -> int:
        maxdist = 0
        cur,prev = 0,0
        tmp = bin(n)[2:]
        while cur != len(tmp):
            if tmp[cur] == '1':
                maxdist = max(maxdist, cur - prev)
                prev = cur
            cur +=1
        return maxdist
        