class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        a=b=0
        for i, j in customers:
            a = max(a, i) + j
            b += a - i
        return b / len(customers)
