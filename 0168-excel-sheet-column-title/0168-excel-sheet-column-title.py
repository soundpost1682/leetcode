class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alpa = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        tmp= ''
        while columnNumber:
            columnNumber -=1
            tmp = alpa[columnNumber % 26] + tmp
            columnNumber //= 26
        return tmp
        