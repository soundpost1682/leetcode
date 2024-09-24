class Solution:
    def checkRecord(self, s: str) -> bool:
        cntA, cntL = 0,0
        for i in s:
            if i=='A': 
                cntA += 1
                cntL = 0
            elif i=='L':
                cntL+=1
            else : cntL=0

            if cntA >=2 or cntL >=3:
                return False
        return True
        

