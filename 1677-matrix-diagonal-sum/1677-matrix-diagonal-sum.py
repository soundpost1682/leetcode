class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        answer = 0
        tmp = len(mat)
        for i in range(tmp):
            answer += mat[i][i]
            answer += mat[i][tmp-i-1]
        if tmp % 2 != 0:
            answer -= mat[tmp//2][tmp//2]
        return answer
        
