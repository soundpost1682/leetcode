class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        emp = sorted(zip(difficulty, profit))
        j = m = answer = 0
        for i in sorted(worker):
            while j < len(emp) and emp[j][0] <= i:
                m = max(m, emp[j][1])
                j += 1
            answer += m
        return answer
        


        
        