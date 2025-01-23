class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        a,b,answer = len(grid), len(grid[0]), 0
        R_cnt = [0]*a
        C_cnt = [0]*b
        for i in range(a):
            for j in range(b):
                if grid[i][j] == 1:
                    R_cnt[i]+=1
                    C_cnt[j]+=1
        for i in range(a):
            for j in range(b):
                if grid[i][j] == 1:
                    if R_cnt[i] >1 or C_cnt[j] > 1:
                        answer +=1
        return answer
