class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n=sorted(nums)
        a,b = 0,len(n)-1
        tmp =0
        while a < b:
            if n[a] + n[b] > k:
                b -= 1
            elif n[a] + n[b] < k:
                a += 1
            else : 
                tmp += 1
                a += 1
                b -= 1
        return tmp

