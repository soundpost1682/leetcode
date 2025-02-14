class Solution:
    def balancedStringSplit(self, s: str) -> int:
        a=b=0
        for i in s:
            if i == 'L': b+=1
            if i == 'R': b-=1
            if b == 0: a+=1
        return a
