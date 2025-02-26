class Solution:
    def finalString(self, s: str) -> str:
        tmp = []
        for i in s:
            if i != 'i':
                tmp.append(i)
            else : tmp.reverse()
        return ''.join(tmp)
        
