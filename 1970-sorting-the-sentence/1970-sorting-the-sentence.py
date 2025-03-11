class Solution:
    def sortSentence(self, s: str) -> str:
        tmp = s.split(' ')
        def number(s):
            return s[-1]
        tmp.sort(key = number)
        def del_num(s):
            return s[:-1]
        fine = map(del_num, tmp)    
        return ' '.join(fine)

        