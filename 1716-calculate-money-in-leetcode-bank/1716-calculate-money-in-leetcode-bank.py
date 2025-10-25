class Solution:
    def totalMoney(self, n: int) -> int:
        tmp , ans, i = n,0,0
        while i <= n //7:
            k = i+1
            if tmp //7 == 0:
                for j in range(tmp):
                    ans +=k
                    k +=1
            else :
                for j in range(7):
                    ans += k
                    k +=1
                tmp -= 7
            i +=1
        return ans
        