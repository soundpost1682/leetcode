class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        tmp, answer = 0, []
        for i in s:
            if i==')': tmp-=1
            if tmp >0: answer.append(i)
            if i=='(': tmp+=1
        return ''.join(answer)
        