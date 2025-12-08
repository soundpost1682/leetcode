class Solution:
    def countTriples(self, n: int) -> int:
        ans =0
        for i in range(1, n):
            for j in range(i+1, n):
                tmp = math.sqrt(i*i + j*j)
                if int(tmp) == tmp and tmp <= n:
                    ans+=2
        return ans
        