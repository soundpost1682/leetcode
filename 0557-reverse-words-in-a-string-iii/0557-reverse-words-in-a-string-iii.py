class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        tmp = [i[::-1] for i in s]
        return ' '.join(tmp)


