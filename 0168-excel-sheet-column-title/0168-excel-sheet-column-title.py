class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        answer =''
        while columnNumber > 0:
            columnNumber -= 1
            tmp = columnNumber % 26
            answer = chr(65+tmp) + answer
            columnNumber //= 26
        return answer
        
