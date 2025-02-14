class Solution:
    def balancedStringSplit(self, s: str) -> int:
        a=b=0
        for i in s:
            b +=1 if i =='R' else -1
            if not b: a+=1
        return a
        