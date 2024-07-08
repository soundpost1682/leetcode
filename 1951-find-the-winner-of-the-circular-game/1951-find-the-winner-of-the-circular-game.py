class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        tmp =0
        for i in range(2, n+1):
            tmp = (k + tmp) % i
        return tmp + 1
        