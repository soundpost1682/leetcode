class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        answer =0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                answer += customers[i]
        
        no = 0
        for i in range(minutes):
            if grumpy[i] ==1:
                no += customers[i]
        
        m = no
        for i in range(minutes, len(customers)):
            if grumpy[i - minutes] ==1:
                no -= customers[i - minutes]
            if grumpy[i] == 1:
                no += customers[i]
            m = max(m, no)
        return answer + m

