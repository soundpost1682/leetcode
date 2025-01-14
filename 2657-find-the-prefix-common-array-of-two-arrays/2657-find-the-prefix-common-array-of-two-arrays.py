class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        L = len(A)
        x, y = {},{}
        for i in range(L):
            x[A[i]] = i
            y[B[i]] = i
            print(x)
        tmp = [0] * L
        for i in range(L):
            cnt=0
            for j in range(i+1):
                if x[A[j]] <= i and y[A[j]] <= i:
                    cnt +=1
            tmp[i] = cnt
        return tmp
        