class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        D = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]        
        saw= set()
        for word in words:
            ans=''
            for mose in word:
                ans += D[ord(mose)-97]
            saw.add(ans)
        return len(saw)

                