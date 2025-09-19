class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        tmp = text.split()
        ans =0
        for i in tmp:
            for j in brokenLetters:
                if j in i: break
            else : ans+=1
        return ans
        
                    


