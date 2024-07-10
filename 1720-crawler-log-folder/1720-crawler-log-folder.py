class Solution:
    def minOperations(self, logs: List[str]) -> int:
        tmp =0
        for i in logs:
            if i == '../':
                if tmp > 0:
                    tmp -= 1
            elif i != './':
                tmp += 1
        return tmp
        
            