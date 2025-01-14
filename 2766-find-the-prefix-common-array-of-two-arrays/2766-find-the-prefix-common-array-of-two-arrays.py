class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        L = len(A)
        x, y = {},{}
        ar = [0] * (L+1)
        ans = [0]*L
        cnt =0
        for i in range(L):
            ar[A[i]] += 1
            if ar[A[i]] == 2:cnt+=1

            ar[B[i]] += 1
            if ar[B[i]] == 2:cnt+=1

            ans[i] = cnt
        return ans
