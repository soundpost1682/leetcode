class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vo = 'aeiou'
        window = answer = 0
        for ch in range(len(s)):
            window += s[ch] in vo
            if ch >= k:
                window -= s[ch - k] in vo
            answer = max(answer, window)
        return answer
        
