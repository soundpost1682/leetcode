class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        k = celsius + 273.15
        ans=[]
        fa = celsius*1.80+32
        ans.append(k)
        ans.append(fa)
        return ans
