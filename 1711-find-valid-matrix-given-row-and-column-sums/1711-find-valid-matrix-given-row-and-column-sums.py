class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ro, co= len(rowSum), len(colSum)
        tmp= [[0] * co for _ in range(ro)]
        i, j=0,0
        while i < ro and j < co:
            a = min(rowSum[i] , colSum[j])
            tmp[i][j] = a
            rowSum[i] -= a
            colSum[j] -= a
            i += (rowSum[i] == 0)
            j += (colSum[j] == 0)
        return tmp
