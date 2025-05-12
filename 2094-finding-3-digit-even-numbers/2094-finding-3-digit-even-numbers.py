class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        tmp = Counter(map(str, digits))
        return [i for i in range(100,1000, 2) if tmp >= Counter(str(i))]
        
