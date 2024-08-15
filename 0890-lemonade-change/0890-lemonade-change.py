class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiv , ten = 0,0
        for note in bills:
            if note == 5: 
                fiv += 1
            elif note == 10: 
                fiv -=1
                ten +=1
            elif ten :
                ten -=1
                fiv -=1
            else : fiv -= 3
            if fiv < 0: 
                return False
        return True



