class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        answer =''
        for i in s:
            if i == '(':
                st.append(answer)
                answer = ''
            elif i == ')':
                answer = answer[::-1]
                answer = st.pop() + answer
            else:
                answer += i
        return answer
        