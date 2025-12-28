class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ro = len(grid)
        co = len(grid[0])
        a,b,cnt = 0, co-1, 0

        while a < ro and b >= 0:
            if grid[a][b] < 0:
                cnt += (ro-a)
                b -=1
            else : a +=1
        return cnt
        