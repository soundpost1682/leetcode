class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        M = S = tmp = 0
        for i in range(len(customers)):
            if not grumpy[i]:
                S += customers[i]
                customers[i] =0
            else: tmp += customers[i]
            if i >= minutes: 
                tmp -= customers[i-minutes]
            M = max(M, tmp)
        return S+M
        
