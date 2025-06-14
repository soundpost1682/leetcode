class Solution:
    def minMaxDifference(self, num: int) -> int:
        st = str(num)
        t,tmp=st,0
        while tmp < len(st) and st[tmp] == '9':
            tmp +=1
        if tmp < len(st):
            st = st.replace(st[tmp], '9')
        t = t.replace(t[0], '0')
        return int(st) - int(t)
        