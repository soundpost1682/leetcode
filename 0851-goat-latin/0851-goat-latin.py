class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s = sentence.split()
        vo = 'aeiouAEIOU'
        ans =[]
        for i,v in enumerate(s):
            if v[0] in vo:
                tmp = v+'ma'
            else:
                tmp = v[1:] + v[0] + 'ma'
            
            tmp += 'a' * (i+1)
            ans.append(tmp)
        return ' '.join(ans)
        