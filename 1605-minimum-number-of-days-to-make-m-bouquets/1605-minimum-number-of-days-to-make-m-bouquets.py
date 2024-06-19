class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def HELP(day: int)-> bool:
            s = ''.join(['X' if i <= day else ' ' for i in bloomDay])
            return s.count('X' *k) >= m
        n, mi, ma = len(bloomDay), min(bloomDay), max(bloomDay)+1
        if n < m*k : return -1
        return mi + bisect_left(range(mi, ma), True, key=HELP)
