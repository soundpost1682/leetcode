class Solution:
    def maxFreqSum(self, s: str) -> int:
        co, vo = 0,0
        saw = set(s)
        for i in saw:
            if i in 'aeiou':
                vo = max(vo, s.count(i))
            else : 
                co = max(co, s.count(i))
        return co + vo
        