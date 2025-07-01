class Solution:
    def possibleStringCount(self, word: str) -> int:
        tmp=1
        for i in range(1, len(word)):
            if word[i] == word[i-1]:
                tmp+=1
        return tmp
        