class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        cnt=0
        for i in range(low, high+1):
            s = str(i)
            if len(s) % 2==0:
                tmp = len(s)//2
                if sum(map(int, s[:tmp])) == sum(map(int, s[tmp:])):
                    cnt+=1
        return cnt
