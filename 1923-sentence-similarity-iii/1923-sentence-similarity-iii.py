class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        a = sentence1.split()
        b = sentence2.split()
        x,y = len(a), len(b)
        if x>y: 
            x,y = y,x
            a,b = b,a
        tmp = 0
        while tmp < x and a[tmp] == b[tmp]:
            tmp+=1
        while tmp < x and a[tmp] == b[y-x+tmp]:
            tmp+=1
        
        return tmp==x
