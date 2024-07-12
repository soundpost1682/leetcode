class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a , b= {},{}
        for ch in s:
            if ch not in a:
                a[ch] = 1
            else: a[ch] += 1
        for ch in t:
            if ch not in b:
                b[ch] = 1
            else: b[ch] += 1
        return a == b
