class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        tmp =0
        for i in range(len(points)-1):
            po = points[i]
            nxt = points[i+1]
            tmp += max(abs(nxt[0] - po[0]), abs(nxt[1] - po[1]))
        return tmp
        
