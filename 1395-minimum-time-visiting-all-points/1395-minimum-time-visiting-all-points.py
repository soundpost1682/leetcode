class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer =0
        for i in range(len(points)-1):
            a, b = points[i]
            x,y = points[i+1]
            answer += max(abs(x-a), abs(y-b))
        return answer
