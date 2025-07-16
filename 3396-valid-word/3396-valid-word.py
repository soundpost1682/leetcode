class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) <3: return False
        vo,co=0,0
        vowels = {'a','e','i','o','u'}
        for i in word:
            if not i.isalnum(): return False
            if i.isalpha():
                if i.lower() in vowels: vo+=1
                else : co+=1
        return vo >0 and co >0
        