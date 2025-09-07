class Solution:
    def sumZero(self, n: int) -> List[int]:
        tmp = [0] * n
        z = 1
        for i in range(n//2):
            tmp[i] = z
            tmp[n-1-i] = -z
            z+=1
        return tmp
