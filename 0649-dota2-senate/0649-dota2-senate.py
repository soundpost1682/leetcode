class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        y = len(senate)
        R_ar = [i for i in range(y) if senate[i] == 'R']
        D_ar = [k for k in range(y) if senate[k] == 'D']

        while R_ar and D_ar :
            R = R_ar.pop(0)
            D = D_ar.pop(0)
            if R < D : R_ar.append(y+R)                
            else : D_ar.append(y+D)

        return 'Radiant' if R_ar else 'Dire'


