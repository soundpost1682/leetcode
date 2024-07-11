class Solution:
    def reverseParentheses(self, s: str) -> str:
        st=[]
        rever=[]
        for i in range(len(s)):
            if s[i] == ')':
                p = st.pop()
                while p != '(':
                    rever.append(p)
                    p = st.pop()
                st += rever
                rever = []
            else:
                st.append(s[i])
        return ''.join(st)
        
