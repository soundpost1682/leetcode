class Solution:
    def sortSentence(self, s: str) -> str:
        tmp = s.split()
        d = {}
        for i in tmp:
            d[i[-1]] = i[:-1]
            

        return ' '.join(d[j] for j in sorted(d))

