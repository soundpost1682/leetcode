class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k %2 ==0 or k%5 == 0: return -1
        tmp = 1 % k
        ans = 1
        while tmp > 0:
            tmp = (tmp * 10+1) % k
            ans +=1
            if ans > k: return -1
        return ans
        
