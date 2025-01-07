class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        tmp = ' '.join(words)
        ans = [i for i in words if tmp.count(i) > 1]
        return ans
        
