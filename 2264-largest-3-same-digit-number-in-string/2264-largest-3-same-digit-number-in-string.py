class Solution:
    def largestGoodInteger(self, num: str) -> str:
        tmp=''
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                tmp = max(tmp, num[i:i+3])
        return tmp
        