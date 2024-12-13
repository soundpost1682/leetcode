class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        st = sentence.split(' ')
        for i, v in enumerate(st):
            if v.startswith(searchWord) :
                return i+1
        return -1

