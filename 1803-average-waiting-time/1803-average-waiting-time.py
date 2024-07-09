class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ar=[]
        tmp =0
        for i, j in customers:
            if i > tmp : tmp = i+j
            else: tmp += j
            ar.append(tmp-i)
        return sum(ar) / len(customers)
        