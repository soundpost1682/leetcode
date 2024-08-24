class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer =0
        for i in range(len(points)-1):
            spot = points[i]
            nextspot = points[i+1]
            answer += max(abs(nextspot[0] - spot[0]), abs(nextspot[1] - spot[1]))
        return answer



        
        
        #     a, b = points[i]
        #     x,y = points[i+1]
        #     answer += max(abs(x-a), abs(y-b))
        # return answer
