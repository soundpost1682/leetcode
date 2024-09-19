class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        w1 = s1.split()
        w2 = s2.split()
        allw = w1+w2
        cnt = Counter(allw)
        return [w for w in cnt if cnt[w] == 1]
