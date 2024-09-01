class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        tmp =[]
        for i in range(0, len(original), n):
            tmp.append(original[i:i+n])
        if m*n != len(original): return []
        return tmp
        
