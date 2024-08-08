class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for amu in words:
            if amu == amu[::-1]:
                return amu
        return ''
        