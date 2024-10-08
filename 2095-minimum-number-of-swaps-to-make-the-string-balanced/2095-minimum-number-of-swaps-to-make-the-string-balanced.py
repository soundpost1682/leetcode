class Solution:
    def minSwaps(self, s: str) -> int:
        tmp = 0
        for i in s:
            if i =='[':
                tmp +=1
            elif tmp > 0:
                tmp -=1
        return (tmp+1) //2
        