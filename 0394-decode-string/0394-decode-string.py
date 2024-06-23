class Solution:
    def decodeString(self, s: str) -> str:
        tmp=[]
        s2, time = '', 0
        for i in s:
            if i.isdigit():
                time = time *10 + int(i)
            elif i == '[':
                tmp.append(s2)
                tmp.append(time)
                s2 =''
                time=0
            elif i.isalpha():
                s2 += i
            elif i==']':
                tmp2=tmp.pop()
                tmp3=tmp.pop()
                s2 = tmp3 + tmp2 * s2
        return s2
