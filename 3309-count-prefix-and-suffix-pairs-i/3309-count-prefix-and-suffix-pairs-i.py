class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        for i, v in combinations(words, 2):
            ans+= v.startswith(i) and v.endswith(i)
        return ans
